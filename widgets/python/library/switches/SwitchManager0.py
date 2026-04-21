import sys, os
class SwitchManager:
	def __init__(self, Switches=None, Triggers=None, Help=None, command=None, c=None, cmd=None):
		if not cmd is None: command = cmd
		if not c is None: command = c
		if command is None and Switches is None and Triggers is None:
			color("SwitchManager args:     Switches, Triggers, command",c='red',p=1)
			command = sys.argv[1:] if len(sys.argv) > 1 else []
		if isinstance(command, int):
			command = sys.argv[command:]
		elif isinstance(command, str):
			command = command.replace('  ', ' ').split(' ')
		elif not command:
			command = sys.argv

		self.command = command
		self.app = command[0]
		self.args = command[1:]

		if Switches is None:
			Switches = {}
		if Triggers is None:
			Triggers = {}
		self.triggers = {**Triggers}
		if Help is None: Help = {}
		self.Help = Help
		self.Switches = Switches
		self.possibleList()

		self.switchesRegister = self._flatten_switches(self.Switches)
		if not 'Help' in self.switchesRegister:
			self.switchesRegister['Help'] = '?,-h,--help,?h,?help'
		if not 'Help' in self.triggers:
			self.triggers['Help'] = self.help

		self.used = {}
		self._Values = {}
		self.usage = {}
		self.instances = {}

		# ---------- ADDED for occurrence grouping ----------
		# Per-occurrence buckets and order per switch
		# _occ_buckets: { name: { flag: [ [vals1], [vals2], ... ] } }
		# _occ_sequence: { name: [ (flag, idx), ... ] } in the order seen
		self._occ_buckets = {}
		self._occ_sequence = {}
		# ---------------------------------------------------

		self.flag_to_key = {}
		for key, val in self.switchesRegister.items():
			self.used[key] = False
			self._Values[key] = []
			if isinstance(val, str):
				val = ' '.join(val.split()).replace(' ', ',')
				self.switchesRegister[key] = val
			for flag in self.switchesRegister[key].split(','):
				self.flag_to_key[flag] = key

		self.parse()
		if 'Help' in self.usage:
			if 'Help' in self._Values and self._Values['Help'] and type(self._Values['Help']) == list:
				self.triggers['Help'](self._Values['Help'][0])
			else:
				self.triggers['Help']()

		# self.usage[key].append(flag)
		# self._Values[key].append(flag)

	def help(self,full=None):
		if full:
			self.validate()
			print('\n\n')

		isGrouped = False
		if type(self.Switches[next(iter(self.Switches))]) == dict:
			isGrouped = True

		if not isGrouped:
			table = []
			for key in self.Switches:
				rec = {}
				rec['name'] = key
				rec['switch'] = self.Switches[key]
				if self.Help:
					if key in self.Help:
						rec['help'] = self.Help[key]
					else:
						rec['help'] = ''
				table.append(rec)

			# settings = dicGen('fields.cols.help.case', 'upper')
			pt(table,'switches',settings)

		elif isGrouped:

			tables = {}
			for group in self.Switches:
				tables[group] = []
				for key in self.Switches[group]:
					rec = {}
					rec['name'] = key
					rec['switch'] = self.Switches[group][key]
					if self.Help:
						if key in self.Help:
							rec['help'] = self.Help[key]
						else:
							rec['help'] = ''
					tables[group].append(rec)
			pt(tables,'switches')
		sys.exit(0)



	def possibleList(self):
		isGrouped = False
		if type(self.Switches[next(iter(self.Switches))]) == list:
			isGrouped = True
		elif not type(self.Switches) == list: return
		global trig

		Switches = self.Switches.copy()
		self.Switches = {}

		if not isGrouped:
			for rec in Switches:
				self.Switches[rec['n']] = rec['s']
				if 't' in rec:
					if type(rec['t']) == str:
						if rec['t'] in globals() and callable(globals()[rec['t']]):
							rec['t'] = eval(rec['t'])
						elif rec['t'] in trig and callable(trig[rec['t']]):
							rec['t'] = trig[rec['t']]
					self.triggers[rec['n']] = rec['t']
				if 'h' in rec:
					self.Help[rec['n']] = rec['h']

		elif isGrouped:
			for group in Switches:
				self.Switches[group] = {}
				for rec in Switches[group]:
					self.Switches[group][rec['n']] = rec['s']
					if 't' in rec:

						if type(rec['t']) == str:
							if rec['t'] in globals() and callable(globals()[rec['t']]):
								rec['t'] = eval(rec['t'])
							elif rec['t'] in trig and callable(trig[rec['t']]):
								rec['t'] = trig[rec['t']]
						self.triggers[rec['n']] = rec['t']
					if 'h' in rec:
						self.Help[rec['n']] = rec['h']

	def _flatten_switches(self, switches):

		flat = {}
		for group_or_key, val in switches.items():
			if isinstance(val, dict):
				flat.update(val)
			else:
				flat[group_or_key] = val
		return flat

	def _clean_quotes(self, value):
		if not isinstance(value, str):
			return value
		for quote in ["'", '"']:
			if value.startswith(quote * 2) and value.endswith(quote * 2):
				value = value[2:-2]
			elif value.startswith(quote) and value.endswith(quote):
				value = value[1:-1]
		return value

	def unset(self, name, instance=None):
		"""Clear usage data for a switch, optionally just for one instance (flag)."""
		if name in self.used:
			self.used[name] = False

		if instance is None:
			self._Values[name] = []
			self.usage.pop(name, None)

			# ---------- ADDED for occurrence grouping ----------
			self._occ_buckets.pop(name, None)
			self._occ_sequence.pop(name, None)
			# ---------------------------------------------------

			self.instances.pop(name, None)
		else:
			if name in self.usage:
				self.usage[name] = [i for i in self.usage[name] if i != instance]
				if not self.usage[name]:
					self.usage.pop(name)
			if name in self.instances and instance in self.instances[name]:
				self.instances[name].pop(instance)
			if name in self.instances and not self.instances[name]:
				self.instances.pop(name)

			# ---------- ADDED for occurrence grouping ----------
			if name in self._occ_buckets and instance in self._occ_buckets[name]:
				# Drop sequence entries referencing this flag
				if name in self._occ_sequence:
					self._occ_sequence[name] = [
						(f, idx) for (f, idx) in self._occ_sequence[name] if f != instance
					]
					if not self._occ_sequence[name]:
						self._occ_sequence.pop(name)
				self._occ_buckets[name].pop(instance)
				if not self._occ_buckets[name]:
					self._occ_buckets.pop(name)
			# ---------------------------------------------------

			# Don't clear _Values if other instances remain
			self._Values[name] = [
				val for inst in self.instances.get(name, {}).values() for val in (inst if isinstance(inst, list) else [])
			] if name in self.instances else []

	def set(self, name, flag=None, values=None, add=False):
		"""Add switch usage manually (values can be list or single)."""

		# next(iter(self.Switches))
		if type(flag) == int:
			if name in self.switchesRegister:
				flag = self.switchesRegister[name].split(',')[flag].strip()
				flagFixed = True
		elif not flag:
			flagFixed = False
			if name in self.instances:
				flag = next(iter(self.instances[name]))
				flagFixed = True
			if not flagFixed and name in self.switchesRegister:
				flag = self.switchesRegister[name].split(',')[0].strip()
				flagFixed = True

		if not add:
			self.unset(name, flag)

		self.used[name] = True
		if name not in self._Values or self._Values[name] is True:
			self._Values[name] = []
		if isinstance(values, str):
			values = [values]
		elif values is None:
			values = []

		if name not in self.usage:
			self.usage[name] = []
		if flag not in self.usage[name]:
			self.usage[name].append(flag)

		if name not in self.instances:
			self.instances[name] = {}
		if flag not in self.instances[name]:
			self.instances[name][flag] = []

		# ---------- ADDED for occurrence grouping ----------
		if name not in self._occ_buckets:
			self._occ_buckets[name] = {}
		if flag not in self._occ_buckets[name]:
			self._occ_buckets[name][flag] = []
		# Start a new occurrence bucket if we're not "adding" to an existing one
		if not add or not self._occ_buckets[name][flag]:
			self._occ_buckets[name][flag].append([])
			if name not in self._occ_sequence:
				self._occ_sequence[name] = []
			self._occ_sequence[name].append((flag, len(self._occ_buckets[name][flag]) - 1))
		# ---------------------------------------------------

		for val in values:
			cleaned = self._clean_quotes(val)
			if name in self.triggers:
				cleaned = self.triggers[name](cleaned)
			self._Values[name].append(cleaned)
			self.instances[name][flag].append(cleaned)

			# ---------- ADDED for occurrence grouping ----------
			self._occ_buckets[name][flag][-1].append(cleaned)
			# ---------------------------------------------------

	def parse(self,args=None, reset=False):
		current_switch = None
		current_key = None
		i = 0

		if args is None:
			args = self.args

		while i < len(args):
			arg = self.args[i]

			# Handle --flag=value format
			if arg.startswith('--') and '=' in arg:
				flag, val = arg.split('=', 1)
				key = self.flag_to_key.get(flag)
				if key:
					current_key = key
					current_switch = flag
					self._register_usage(key, current_switch)
					values = val.split(',')
					for v in values:
						value = self.triggers[key](v) if key in self.triggers else v
						value = self._clean_quotes(value)
						self._Values[key].append(value)
						self.instances[key][current_switch].append(value)

						# ---------- ADDED for occurrence grouping ----------
						self._occ_buckets[key][current_switch][-1].append(value)
						# ---------------------------------------------------

			# Handle standalone flags like -pulldown or -m
			elif arg in self.flag_to_key:
				key = self.flag_to_key[arg]
				current_key = key
				current_switch = arg
				self._register_usage(key, current_switch)
				if self._Values[key] == []:
					self._Values[key] = True

			# Handle values passed after a flag
			elif current_key and current_switch:
				if self._Values[current_key] is True:
					self._Values[current_key] = []
				value = self.triggers[current_key](arg) if current_key in self.triggers else arg
				value = self._clean_quotes(value)
				self._Values[current_key].append(value)
				self.instances[current_key][current_switch].append(value)

				# ---------- ADDED for occurrence grouping ----------
				self._occ_buckets[current_key][current_switch][-1].append(value)
				# ---------------------------------------------------

			# Orphan value (no active flag) — ignored, or could log
			else:
				pass

			i += 1

	def _register_usage(self, key, flag):
		self.used[key] = True
		if key not in self.instances:
			self.instances[key] = {}
		if flag not in self.instances[key]:
			self.instances[key][flag] = []
		if key not in self.usage:
			self.usage[key] = []
		if flag not in self.usage[key]:
			self.usage[key].append(flag)

		# ---------- ADDED for occurrence grouping ----------
		if key not in self._occ_buckets:
			self._occ_buckets[key] = {}
		if flag not in self._occ_buckets[key]:
			self._occ_buckets[key][flag] = []
		# start a NEW bucket for this occurrence
		self._occ_buckets[key][flag].append([])
		occ_idx = len(self._occ_buckets[key][flag]) - 1

		if key not in self._occ_sequence:
			self._occ_sequence[key] = []
		self._occ_sequence[key].append((flag, occ_idx))
		# ---------------------------------------------------

	def isActive(self, name, instance=None):
		if name not in self.used or not self.used[name]:
			return False
		if instance is None:
			return True
		return instance in self.usage.get(name, [])

	def data(self, what, name, instance=None):
		if what == 0: what = 'name'
		elif what == 1: what = 'data'
		val = self.values(name, instance)
		if not val:
			global PIPE
			return PIPE if PIPE else []
		elif what == 'data':
			os=imp('os.path.isfile')
			if os.path.isfile(val[0]):
				with open(val[0], 'r') as f:
					return f.read().splitlines()
			return val

		return val

	def values(self, name, instance=None):
		if not instance is None: return self.Values(name, instance)
		val = self._Values.get(name, [])
		if val is True:
			return []
		return val

	def value(self, name):
		vals = self.values(name)
		if len(vals) == 1:
			return vals[0]
		return ','.join(vals)

	def Values(self, name, instance=None):
		if name not in self.instances:
			return []
		if instance is not None:
			return self.instances[name].get(instance, [])
		return self.values(name)

	# ---------- ADDED: accessor for grouped-by-occurrence ----------
	def Instances(self, name, instance=None):
		"""
		Return grouped occurrences for a switch.

		- Instances('Has') -> list of lists in global occurrence order across all flags
		- Instances('Has', '-and') -> list of lists for that flag only (each occurrence)
		- Instances('Has', '-or') -> list of lists for that flag only
		"""
		if name not in self._occ_buckets:
			return []
		if instance is None:
			if name not in self._occ_sequence:
				return []
			out = []
			for (flag, idx) in self._occ_sequence[name]:
				bucket_list = self._occ_buckets[name].get(flag, [])
				if 0 <= idx < len(bucket_list):
					out.append(bucket_list[idx])
			return out
		else:
			return list(self._occ_buckets[name].get(instance, []))
	# ---------------------------------------------------------------

	def strip(self):
		return [item for item in self.command if item not in self.flag_to_key]

	def resetState(self):
		self.used = {}
		self._Values = {}
		self.usage = {}
		self.instances = {}
		# ---------- ADDED for occurrence grouping ----------
		self._occ_buckets = {}
		self._occ_sequence = {}
		# ---------------------------------------------------
		for key in self.switchesRegister:
			self.used[key] = False
			self._Values[key] = []

	def validate(self):
		import json
		color('___________\nApp:',c='cyan')
		color(self.app, c='yellow')
		color('___________\nUsed:',c='cyan')
		color(json.dumps(self.used, indent=4), c='yellow')
		color('___________\nValues:',c='cyan')
		color(json.dumps(self._Values, indent=4), c='yellow')
		color('___________\nUsage:',c='cyan')
		color(json.dumps(self.usage, indent=4), c='yellow')
		color('___________\nInstances:',c='cyan')
		color(json.dumps(self.instances, indent=4), c='yellow')

	def dump(self):
		return {
			'command': self.command,
			'app': self.app,
			'used': self.used,
			'values': self._Values,
			'usage': self.usage,
			'instances': self.instances
		}
def color(text, c=None, p=0): pass
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
#n)--> start

def fromYML(text):
    if os.path.isfile(text):
        with open(text, 'r') as file: content = file.read()
        return content
    elif not '\n' in text and text.count(os.sep):
            return {}
    try:
        import yaml # type: ignore
        return yaml.safe_load(text.replace('\t','    '))
    except Exception as e:
        table = {}
        lines = text.split('\n')
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                table[key.strip()] = value.strip()
            return table

def y(_yaml,p=False):
        while ' ||' in _yaml:
            _yaml = _yaml.replace(' ||', '||')
        while '|| ' in _yaml:
            _yaml = _yaml.replace('|| ', '||')
        _yaml = _yaml.replace('||','|')
        _yaml = _yaml.replace('|','\n')
        if p:
            print(_yaml)
        return fromYML(_yaml)
