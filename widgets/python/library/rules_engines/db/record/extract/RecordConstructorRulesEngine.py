#!/usr/bin/env python3

from pathlib import Path
import re
import yaml


# =========================
# CONFIG
# =========================

INPUT_FILE = "1778694366.txt"
# INPUT_FILE = "./parsed/1778694366.txt"

INPUT_FOLDER = "./parsed"
OUTPUT_FOLDER = "./yaml"

Add_GPS = False

# class Runtime: pass


class RecordConstructorRulesEngine:

	fn = {}
	# runtime = Runtime()
	runtime = type('Runtime', (), {})()

	orderDefault = [
		"after",
		"after-inline",
		"before",
		"split",
		"iter",
		"join-lines",
		"join",
		"int",
		"trigger",
		"callback",
	]

	def __init__(self, rules):
		self.rules = self.normalize(rules)
		self.reset_runtime()

	def reset_runtime(self):
		self.runtime.output = {}
		self.runtime.data = {}
		self.runtime.meta = {}
		self.runtime.lines = []
		self.runtime.spent = set()
		self.runtime.matches = {}

	@staticmethod
	def normalize(dic):
		if isinstance(dic, dict):
			out = {}

			for k, v in dic.items():

				if k == "int":
					out[k] = RecordConstructorRulesEngine.normalize_int(v)

				elif k in {"split", "join", "join-lines"}:
					out[k] = RecordConstructorRulesEngine.normalize_by(v)

				elif k in {"after", "before", "after-inline"}:
					out[k] = RecordConstructorRulesEngine.normalize_text(v)

				elif k == "iter":
					out[k] = RecordConstructorRulesEngine.normalize_iter(v)

				else:
					out[k] = RecordConstructorRulesEngine.normalize(v)

			return out

		if isinstance(dic, list):
			return [RecordConstructorRulesEngine.normalize(x) for x in dic]

		return dic

	@staticmethod
	def normalize_int(v):
		if isinstance(v, dict):
			return v

		if isinstance(v, int):
			return {"length": v}

		if isinstance(v, (list, tuple)) and len(v) == 2:
			return {"length-range": [int(v[0]), int(v[1])]}

		if isinstance(v, str) and "-" in v:
			a, b = v.split("-", 1)
			return {"length-range": [int(a), int(b)]}

		return {"length": int(v)}

	@staticmethod
	def normalize_by(v):
		if isinstance(v, dict):
			return v

		return {"by": v}

	@staticmethod
	def normalize_text(v):
		if isinstance(v, dict):
			return v

		return {"text": v}

	@staticmethod
	def normalize_iter(v):
		if isinstance(v, dict):
			return v

		if isinstance(v, (list, tuple)):
			return {"take": list(v)}

		return {"take": [v]}


	def process_file(self, input_file):
		input_path = Path(input_file).expanduser()

		self.runtime.meta['input_file'] = str(input_path)

		text = input_path.read_text(
			encoding="utf-8",
			errors="replace"
		)

		return self.process_text(text)

	def process_file_to_yaml_dir(self, input_file, input_folder=None, output_folder=None):
		input_path = Path(input_file).expanduser()

		if not input_path.is_absolute():
			input_path = Path(input_folder or ".").expanduser() / input_path

		text = input_path.read_text(encoding="utf-8", errors="replace")
		output = self.process_text(text)

		if output_folder:
			out_dir = Path(output_folder).expanduser()
			out_dir.mkdir(parents=True, exist_ok=True)
			out_path = out_dir / (input_path.stem + ".yml")
			out_path.write_text(yaml.safe_dump(output, sort_keys=False), encoding="utf-8")
			return output, out_path

		return output, None





	def process_text(self, text):
		self.reset_runtime()

		raw_lines = text.splitlines()
		self.runtime.lines = raw_lines
		self.runtime.meta["raw_text"] = text

		self.process_numbered_lines()
		self.process_find_rules(text)
		self.process_star_rule()
		self.process_final_rule()

		return self.runtime.output

	def clean_line(self, value):
		return str(value).strip()


	def process_numbered_lines(self):
		for key, rule in self.rules.items():
			if not isinstance(key, int):
				continue

			if key == 0:
				continue

			index = key - 1
			value = self.runtime.lines[index] if index < len(self.runtime.lines) else ""
			self.runtime.spent.add(index)

			rules = rule if isinstance(rule, list) else [rule]

			for one_rule in rules:

				if isinstance(one_rule, str):
					self.runtime.output[one_rule] = self.clean_line(value)
					continue

				if isinstance(one_rule, dict):
					field = one_rule.get("name") or one_rule.get("field")

					parsed_value = self.apply_rule(value, one_rule)

					if parsed_value is not None and field:
						self.runtime.output[field] = parsed_value

					self.apply_callback(parsed_value, one_rule)


	def process_numbered_lines__old(self):
		for key, rule in self.rules.items():
			if not isinstance(key, int):
				continue

			if key == 0:
				continue

			index = key - 1
			value = self.runtime.lines[index] if index < len(self.runtime.lines) else ""
			self.runtime.spent.add(index)

			if isinstance(rule, str):
				self.runtime.output[rule] = self.clean_line(value)
				continue

			if isinstance(rule, dict):
				field = rule.get("name") or rule.get("field")
				value = self.apply_rule(value, rule)

				if value is not None and field:
					self.runtime.output[field] = value





	def process_find_rules(self, text):
		for rule in self.rules.get("find", []):
			name = rule.get("name") or rule.get("field")

			candidates = self.find_candidates(text, rule)

			for value in candidates:
				original = value
				value = self.apply_rule(value, rule)

				if value in [None, ""]:
					continue

				ok, value = self.apply_trigger(value, rule)

				if not ok:
					continue

				if name:
					self.runtime.output[name] = value
					self.runtime.matches[name] = original

				self.apply_callback(value, rule)

				break

	def find_candidates(self, text, rule):
		candidates = []

		if "after" in rule or "before" in rule:
			candidates.append(text)
			return candidates

		if "after-inline" in rule:
			marker = rule["after-inline"].get("text", "")
			for line in self.runtime.lines:
				if marker in line:
					candidates.append(line)
			return candidates

		if "int" in rule:
			for line in self.runtime.lines:
				for m in re.findall(r"\b\d+\b", line):
					candidates.append(m)

		return candidates

	def process_star_rule(self):
		if "*" not in self.rules:
			return

		rule = self.rules["*"]
		name = rule.get("name") or rule.get("field")

		leftovers = []

		for i, line in enumerate(self.runtime.lines):
			if i not in self.runtime.spent:
				if line.strip():
					leftovers.append(line.strip())

		if not leftovers or not name:
			return

		if "join-lines" in rule:
			by = rule["join-lines"].get("by", "\n")
			value = by.join(leftovers)
		else:
			value = leftovers

		self.runtime.output[name] = value

	def process_final_rule(self):
		rule = self.rules.get(0)

		if not isinstance(rule, dict):
			return

		cb = rule.get("callback")
		if callable(cb):
			result = cb(self.runtime.output, rule)

			if isinstance(result, dict):
				self.runtime.output.update(result)

	def apply_rule(self, value, rule):
		for key in self.orderDefault:
			if key not in rule:
				continue

			if key in {"trigger", "callback"}:
				continue

			value = self.apply_operation(key, value, rule[key], rule)

			if value is None:
				return None

		return value

	def apply_operation(self, key, value, child, rule):
		if key == "after":
			marker = child.get("text", "")
			if marker not in value:
				return None
			return value.split(marker, 1)[1].strip()

		if key == "before":
			marker = child.get("text", "")
			if marker not in value:
				return value.strip()
			return value.split(marker, 1)[0].strip()

		if key == "after-inline":
			marker = child.get("text", "")
			if marker not in value:
				return None
			return value.split(marker, 1)[1].strip()

		if key == "split":
			return self.op_split(value, child)

		if key == "iter":
			return self.op_iter(value, child)

		if key == "join-lines":
			by = child.get("by", "\n")
			lines = [x.strip() for x in str(value).splitlines() if x.strip()]
			return by.join(lines)

		if key == "join":
			by = child.get("by", "")
			if isinstance(value, list):
				return by.join([str(x) for x in value])
			return value

		if key == "int":
			return self.op_int(value, child)

		return value

	def op_split(self, value, child):
		if isinstance(child, list):
			out = value
			for item in child:
				out = self.op_split(out, item)
			return out

		by = child.get("by", " ")
		parts = str(value).split(by)

		if "iter" in child:
			return self.op_iter(parts, self.normalize_iter(child["iter"]))

		return parts

	def op_iter(self, value, child):
		take = child.get("take", [])

		if not isinstance(value, list):
			value = str(value).split()

		selected = []

		for i in take:
			try:
				selected.append(value[int(i)].strip())
			except Exception:
				pass

		if len(selected) == 1:
			return selected[0]

		return selected

	def op_int(self, value, child):
		digits = re.sub(r"\D+", "", str(value))

		if "length" in child:
			if len(digits) == int(child["length"]):
				return digits
			return None

		if "length-range" in child:
			a, b = child["length-range"]
			if int(a) <= len(digits) <= int(b):
				return digits
			return None

		return digits

	def apply_trigger(self, value, rule):
		trig = rule.get("trigger")

		if not callable(trig):
			return True, value

		result = trig(value, rule)

		if result is False:
			return False, None

		if result == (False, None):
			return False, None

		if result is None:
			return True, value

		if isinstance(result, tuple):
			ok, new_value = result
			if ok is False:
				return False, None
			return True, new_value

		if isinstance(result, dict):
			self.runtime.output.update(result)
			return True, value

		return True, result

	def apply_callback(self, value, rule):
		cb = rule.get("callback")

		if not callable(cb):
			return

		result = cb(value, rule)

		if isinstance(result, dict):
			self.runtime.output.update(result)


# =========================
# EXAMPLE TRIGGERS / CALLBACKS
# =========================

def account_starts_with_833(value, rule=None):
	value = str(value).strip()

	if not value.startswith("833"):
		return False, None

	return value



def normalize_address_callback(value, rule=None):
	# simple placeholder for later
	# can return a value OR a dict of extra fields
	return value






def final_callback(output, rule=None):
	# simple placeholder for upload/api later
	

	global Add_GPS


	
	# <GPS>
	if Add_GPS:
		import sys, os
		sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'location')))
		from zip_to_gps import zip_to_gps   # type: ignore
		valid = False
		for k in 'address zip postal'.split(' '):
			for kk in output:
				if k.lower() in kk.lower():
					valid = output[kk]
		if valid:
			valid = valid.strip()
			if ' ' in valid: valid = valid.split(' ')[-1]
			valid = valid.split('-')[0]
			# print(valid)

			try:
				location = zip_to_gps( valid )
				# print(location)
				# for z in location: print(z, location[z])
				gps = str(location['latitude']) + ', ' + str(location['longitude'])
			except:
				gps = ''
			if gps:
				output['gps'] = gps

	# </GPS>



	# output["_processed"] = True
	return output

def final_trigger(value, rule=None):
	# simple placeholder for later
	return True


# =========================
# RULE CONFIG
# =========================

examples = {}

examples[1] = {
	0: {
		"callback": final_callback,
	},

	1: "note",

	"*": {
		"name": "notes",
		"join-lines": "\n",
	},

	"find": [
		{
			"name": "job_number",
			"after-inline": "Job #",
			"split": " ",
			"iter": 0,
			"int": 6,
		},

		{
			"name": "work_order",
			"int": 20,
		},

		{
			"name": "account",
			"int": 16,
			"trigger": account_starts_with_833,
		},

		{
			"name": "address",
			"after": "Address",
			"before": "Job Info",
			"join-lines": " ",
			"callback": normalize_address_callback,
		},
	],
}



examples[2] = {
	0: {
		'trigger': final_trigger,
		'callback': final_callback,
	},

	1: 'note',
	# 2: {
	#     'name': 'job_header',
	#     'split': '>',
	#     'iter': [0, 1],
	#     'fields': ['job_type', 'job_reason'],
	# },

	2: [
		{
			'name': 'job_type',
			'split': '>',
			'iter': 0,
		},
		{
			'name': 'job_reason',
			'split': '>',
			'iter': 1,
		},
	],

	3: 'job_number',
	4: 'work_order',
	5: 'account',
	6: 'address',
	7: 'phone',

	'*': {
		'name': 'notes',
		'join-lines': '\n',
	},
}

def clean_note(value, rule=None):
	value = str(value).strip()
	return value

examples[3] = {
	0: {
		'trigger': final_trigger,
		'callback': final_callback,
	},

	1: {
		'name': 'note',
		'callback': clean_note,
	},

	# 2: {
	#     'name': 'job_header',
	#     'split': '>',
	#     'iter': [0, 1],
	#     'fields': ['job_type', 'job_reason'],
	# },

	2: {
		'name': 'job_type',
		'split': '>',
		'iter': 0,
	},

	2: {
		'name': 'job_reason',
		'split': '>',
		'iter': 1,
	},

	3: {
		'name': 'job_number',
		'int': 6,
	},

	4: {
		'name': 'work_order',
		'int': [19, 21],
	},

	5: {
		'name': 'account',
		'int': 16,
		'trigger': account_starts_with_833,
	},

	6: {
		'name': 'address',
		'split': ',',
		'iter': [0, 1, 2, 3],
		'fields': ['address', 'city', 'state', 'zip'],
	},

	7: {
		'name': 'phone',
		'regex': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
	},

	'*': {
		'name': 'notes',
		'join-lines': '\n',
	},

	'find': [
		{
			'name': 'job_number',
			'after-inline': 'Job #',
			'split': ' ',
			'iter': 0,
			'int': 6,
		},

		{
			'name': 'work_order',
			'after': 'Work Order #',
			'before': 'Refresh',
			'int': 20,
		},

		{
			'name': 'account',
			'after': 'Account #',
			'before': 'Connection Type:',
			'int': 16,
			'trigger': account_starts_with_833,
		},

		{
			'name': 'requested_services',
			'after': 'Requested Services',
			'before': 'Address',
			'join-lines': ', ',
		},

		{
			'name': 'address_raw',
			'after': 'Address',
			'before': 'Job Info',
			'join-lines': ' ',
			'callback': normalize_address_callback,
		},

		{
			'name': 'connection_type',
			'after': 'Connection Type:',
			'before': 'Node:',
			'join-lines': ' ',
		},

		{
			'name': 'drop_tag',
			'after': 'Drop Tags:',
			'before': 'Edit',
			'join-lines': ', ',
		},

		{
			'name': 'all_20_digit_numbers',
			'int': 20,
			'join': ' | ',
		},

		{
			'name': 'possible_ids',
			'int': '5-7',
			'join': ', ',
		},

		{
			'name': 'custom_split_take',
			'after-inline': 'Job #',
			'split': [
				{'by': '#', 'iter': 1},
				{'by': ' ', 'iter': 0},
			],
			'int': 6,
		},

		{
			'name': 'textarea_notes',
			'after': 'Common Tasks & Tools',
			'join-lines': '\n',
		},
	],
}


lines = examples[2]

# =========================
# ENGINE
# =========================




from pathlib import Path

def get_files(folder_path, recursive=False, relative=False):
    folder = Path(folder_path)

    files = (
        folder.rglob("*") if recursive
        else folder.iterdir()
    )

    result = [f for f in files if f.is_file()]

    if relative:
        return [str(f.relative_to(folder)) for f in result]

    return [str(f.resolve()) for f in result]

# =========================
# RUN
# =========================



def main():
	import sys
	import os


	engine = RecordConstructorRulesEngine(lines)

	
	
	if os.path.isfile(sys.argv[-1]):
		output = engine.process_file(
			input_file=sys.argv[-1],
		)

		print(yaml.safe_dump(output, sort_keys=False))
		return 0

	
	if os.path.isdir(sys.argv[-1]):
		if os.path.isdir(sys.argv[-2]):
			INPUT_FOLDER = sys.argv[-2]
			OUTPUT_FOLDER = sys.argv[-1]
		else:
			INPUT_FOLDER = sys.argv[-1]

		for fi in get_files(INPUT_FOLDER):
			engine.process_file_to_yaml_dir(
				input_file=fi,
				input_folder=INPUT_FOLDER,
				output_folder=OUTPUT_FOLDER,
			)
			

	
	
	# if out_path: print(f"Saved: {out_path}")



if __name__ == "__main__":
	raise SystemExit(main())