import json
import os
import re
import copy
import glob
import time
import ast
from functools import reduce
from typing import Any, Dict, List, Tuple, Optional, Union


class JsonDatabase2:
	"""
	A lightweight JSON DB with path navigation (dicts + lists), record-style ops on list endpoints,
	file-backed persistence, optional backups, simple transactions, and rule-engine-ready condition ops.

	Root modes:
	- Dict mode: data is a dict at root.
	- Collection mode: data is a list (of dicts or mixed); use path=None or "" to address root list.

	Path syntax:
	- Dot traversal for dicts:   a.b.c
	- Bracket indices for lists: a.b[2].c[0]
	- Escape dot in keys:        settings.theme\.name
	"""

	# ---------------------------
	# Construction & persistence
	# ---------------------------

	def __init__(self, input_data: Union[str, dict, list]):
		self.data: Union[dict, list] = {}
		self.file_path: Optional[str] = None

		# Persistence / backup knobs
		self.backup_dir: str = './.JsonDatabase'
		self.is_file_mode: bool = False
		self.auto_persist: bool = False      # save to file automatically after writes
		self.backups_enabled: bool = False   # whether to write timestamped backups on writes

		# Transactions
		self.transaction_data: Optional[Union[dict, list]] = None

		# Load
		if isinstance(input_data, str):
			if os.path.isfile(input_data):
				self.file_path = input_data
				self.is_file_mode = True
				with open(self.file_path, 'r', encoding='utf-8') as f:
					self.data = json.load(f)
			else:
				try:
					self.data = json.loads(input_data)
				except json.JSONDecodeError:
					raise ValueError("Invalid JSON string provided.")
		elif isinstance(input_data, (dict, list)):
			self.data = input_data
		else:
			raise ValueError("Input must be a file path, JSON string, dict, or list.")

		# Modes
		self.mode: str = 'dict' if isinstance(self.data, dict) else 'list'
		self.auto_persist = self.is_file_mode
		# backups are off by default; call `enableBackups()` to turn on
		# create backup dir lazily

		# Build index (now list-aware)
		self.index: Dict[str, Any] = self.indexJson(self.data)

	def initializeBackupDir(self):
		os.makedirs(self.backup_dir, exist_ok=True)
		ht = os.path.join(self.backup_dir, '.htaccess')
		if not os.path.exists(ht):
			with open(ht, 'w', encoding='utf-8') as f:
				f.write("Deny from all\n")

	def enableBackups(self, enabled: bool = True):
		self.backups_enabled = enabled
		if enabled:
			self.initializeBackupDir()

	def _persist(self):
		"""Persist to file if file-backed and not in a transaction."""
		if self.transaction_data is not None:
			return
		if self.auto_persist and self.is_file_mode and self.file_path:
			self.writeJson(self.data)

	def _maybe_backup(self, path: str, old_data: Any):
		"""Create a backup snapshot of `old_data` at `path` (pre-write)."""
		if self.transaction_data is not None:
			return
		if not self.backups_enabled:
			return
		if not self.backup_dir:
			return
		self.initializeBackupDir()
		safe_dir = os.path.join(self.backup_dir, path.replace('.', os.sep))
		os.makedirs(safe_dir, exist_ok=True)
		ts = time.strftime("%Y%m%d-%H%M%S")
		with open(os.path.join(safe_dir, f"{ts}.json"), 'w', encoding='utf-8') as f:
			json.dump(old_data, f, indent=4)

	# ---------------------------
	# Path parsing & traversal
	# ---------------------------

	_IDX_RE = re.compile(r'\[(\d+)\]')

	def _split_escaped(self, path: str) -> List[str]:
		"""Split on '.' while honoring '\.' escape."""
		if not path:
			return []
		parts = []
		buf = []
		escape = False
		for ch in path:
			if escape:
				buf.append(ch)
				escape = False
			elif ch == '\\':
				escape = True
			elif ch == '.':
				parts.append(''.join(buf)); buf = []
			else:
				buf.append(ch)
		parts.append(''.join(buf))
		return parts

	def _parse_path(self, path: Optional[str]) -> List[Tuple[Optional[str], Optional[int]]]:
		"""
		Convert 'a.b[2].c[0].d' -> [('a', None), ('b', 2), ('c', 0), ('d', None)].
		Empty/None path -> [] (meaning root).
		"""
		if not path:
			return []
		out: List[Tuple[Optional[str], Optional[int]]] = []
		for seg in self._split_escaped(path):
			# Extract key and any indices
			key_match = re.match(r'^([^\[\]]+)', seg)
			key = key_match.group(1) if key_match else None
			idxs = [int(m) for m in self._IDX_RE.findall(seg)]
			if key is not None:
				if idxs:
					out.append((key, idxs[0]))
					for i in idxs[1:]:
						out.append((None, i))
				else:
					out.append((key, None))
			else:
				# only indices (rare), still accept
				for i in idxs:
					out.append((None, i))
		return out

	def _traverse(self, path: Optional[str], create: bool = False,
				ensure_list_final: bool = False) -> Tuple[Optional[Any], Optional[Any], bool]:
		"""
		Traverse to the node indicated by path.
		Returns (parent_ref, last_key_or_index, is_list_final)
		If path is None/empty, returns (None, None, isinstance(self.data, list)).
		"""
		spec = self._parse_path(path)
		if not spec:
			return None, None, isinstance(self.data, list)

		cur = self.data
		parent = None
		last_k = None

		for i, (key, idx) in enumerate(spec):
			is_last = (i == len(spec) - 1)

			# dict step
			if key is not None:
				if not isinstance(cur, dict):
					if not create:
						return None, None, False
					# convert non-dict into dict
					if parent is None:
						# replace the root
						self.data = {}
						cur = self.data
					else:
						parent[last_k] = {}
						cur = parent[last_k]
				if key not in cur:
					if not create:
						return None, None, False
					# create placeholder based on next token if any
					cur[key] = [] if (idx is not None) else ( [] if (is_last and ensure_list_final) else {} )
				parent, last_k = cur, key
				cur = cur[key]

			# list step
			if idx is not None:
				if not isinstance(cur, list):
					if not create:
						return None, None, False
					# convert into list
					parent[last_k] = []
					cur = parent[last_k]
				if idx >= len(cur):
					if not create:
						return None, None, False
					cur.extend([None] * (idx - len(cur) + 1))
				if cur[idx] is None:
					if create:
						cur[idx] = [] if (is_last and ensure_list_final) else {}
					else:
						return None, None, False
				parent, last_k = cur, idx
				cur = cur[idx]

			if is_last:
				return parent, last_k, isinstance(cur, list)

		return parent, last_k, isinstance(cur, list)

	def _get_node(self, path: Optional[str]) -> Any:
		if not path:
			return self.data
		parent, key, _ = self._traverse(path, create=False)
		if parent is None:
			return None
		return parent[key]

	# ---------------------------
	# Indexing
	# ---------------------------

	def indexJson(self, data: Any, prefix: str = '') -> Dict[str, Any]:
		"""
		Creates a flat index of leaf paths -> value. Handles dicts and lists.
		"""
		out = {}
		if isinstance(data, dict):
			for k, v in data.items():
				p = f"{prefix}.{k}" if prefix else k
				if isinstance(v, (dict, list)):
					out.update(self.indexJson(v, p))
				else:
					out[p] = v
		elif isinstance(data, list):
			for i, v in enumerate(data):
				p = f"{prefix}[{i}]" if prefix else f"[{i}]"
				if isinstance(v, (dict, list)):
					out.update(self.indexJson(v, p))
				else:
					out[p] = v
		else:
			if prefix:
				out[prefix] = data
		return out

	# ---------------------------
	# Public API (same names)
	# ---------------------------

	def jsonByPath(self, path: Optional[str]):
		"""Return value at path; None/'' returns the root."""
		return self._get_node(path)

	def deleteMany(self, path: Optional[str], search_conditions=None, omit_conditions=None):
		records = self._get_node(path)
		if records is None:
			return {"error": f"No records found at path: {path}"}
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}

		old = copy.deepcopy(records)
		new_list = [
			r for r in records
			if not (self.matchConditions(r, search_conditions) and not self.matchConditions(r, omit_conditions))
		]
		if len(new_list) == len(records):
			return {"error": "No records matched the deletion criteria"}

		# backup & write
		parent, key, _ = self._traverse(path, create=False)
		if parent is None:
			return {"error": "Internal: could not resolve parent for deletion"}
		self._maybe_backup(path or '', old)
		parent[key] = new_list
		self._persist()
		return {"success": "Records deleted"}

	# -------- Conditions & operators (rules-engine ready) --------

	def matchConditions(self, record: dict, conditions: Optional[dict]) -> bool:
		if conditions is None:
			return True
		if not isinstance(conditions, dict):
			return False
		for field, cond in conditions.items():
			# nested dotted field support
			value = self._get_field(record, field)
			if not self.matchOperator(value, cond):
				return False
		return True

	def matchOperator(self, value: Any, condition: dict) -> bool:
		"""
		Supported:
		'==','!=','<','>','<=','>=',
		'like','ilike','in','nin','exists','regex','contains','any','all'
		"""
		if not isinstance(condition, dict) or not condition:
			return False
		op, expected = next(iter(condition.items()))

		def _cmp(a, b, fn):
			try:
				return fn(a, b)
			except Exception:
				return False

		ops = {
			'==': lambda v: v == expected,
			'!=': lambda v: v != expected,
			'<':  lambda v: _cmp(v, expected, lambda x, y: x < y),
			'>':  lambda v: _cmp(v, expected, lambda x, y: x > y),
			'<=': lambda v: _cmp(v, expected, lambda x, y: x <= y),
			'>=': lambda v: _cmp(v, expected, lambda x, y: x >= y),
			'like':  lambda v: (isinstance(v, str) and isinstance(expected, str) and (expected in v)),
			'ilike': lambda v: (isinstance(v, str) and isinstance(expected, str) and (expected.lower() in v.lower())),
			'in':    lambda v: v in expected if isinstance(expected, (list, set, tuple)) else False,
			'nin':   lambda v: v not in expected if isinstance(expected, (list, set, tuple)) else False,
			'exists': lambda v: bool(v) if expected else (v is None or v == '' or v == [] or v == {}),
			'regex':  lambda v: (isinstance(v, str) and re.search(expected, v) is not None),
			'contains': lambda v: (isinstance(v, (list, set, tuple, dict, str)) and (expected in v if not isinstance(v, dict) else expected in v.keys())),
			'any':   lambda v: any(self.matchOperator(v, c) for c in expected) if isinstance(expected, list) else False,
			'all':   lambda v: all(self.matchOperator(v, c) for c in expected) if isinstance(expected, list) else False,
		}
		fn = ops.get(op)
		if not fn:
			return False
		return fn(value)

	def _get_field(self, obj: Any, dotted: str) -> Any:
		"""
		Get nested value from a dict/list using dotted path and bracket indices.
		E.g., "a.b[2].c".
		"""
		if obj is None:
			return None
		spec = self._parse_path(dotted)
		cur = obj
		for key, idx in spec:
			if key is not None:
				if not isinstance(cur, dict) or key not in cur:
					return None
				cur = cur[key]
			if idx is not None:
				if not isinstance(cur, list) or idx >= len(cur):
					return None
				cur = cur[idx]
		return cur

	# ---------------------------
	# Writes & utilities
	# ---------------------------

	def overwriteEnd(self, path: Optional[str], json_data: str):
		data_to_insert = json.loads(json_data)
		old = copy.deepcopy(self._get_node(path))
		if old is None and path:
			# if path not present, we still back up parent node if resolvable
			parent, key, _ = self._traverse(self._parent_path(path), create=False)
			if parent is not None:
				self._maybe_backup(self._parent_path(path), copy.deepcopy(parent[key]))

		parent, key, _ = self._traverse(path, create=True)
		if parent is None and key is None:
			# replacing root
			if self.backups_enabled:
				self._maybe_backup('(root)', copy.deepcopy(self.data))
			self.data = data_to_insert
		else:
			if path:
				self._maybe_backup(path, old)
			parent[key] = data_to_insert
		self.index = self.indexJson(self.data)
		self._persist()

	def writeJson(self, data):
		if not self.file_path:
			return
		with open(self.file_path, 'w', encoding='utf-8') as f:
			json.dump(data, f, indent=4)

	def aggregate(self, path: Optional[str], operation: str, field: str,
				search_conditions=None, omit_conditions=None):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "No records list found for aggregate"}

		filtered = [
			r.get(field) for r in records
			if self.matchConditions(r, search_conditions)
			and not self.matchConditions(r, omit_conditions)
			and isinstance(r.get(field), (int, float))
		]
		if operation == "sum":
			return sum(filtered) if filtered else 0
		if operation == "avg":
			return (sum(filtered) / len(filtered)) if filtered else 0
		if operation == "min":
			return min(filtered) if filtered else None
		if operation == "max":
			return max(filtered) if filtered else None
		if operation == "count":
			return len(filtered)
		return {"error": "Invalid operation"}

	def findSorted(self, path: Optional[str], sort_field: str, sort_order='asc',
				search_conditions=None, omit_conditions=None):
		recs = self.find(path, search_conditions, omit_conditions)
		if isinstance(recs, dict) and "error" in recs:
			return recs
		reverse = (sort_order == 'desc')
		# Stable sort with None-last handling
		def keyfn(x):
			v = self._get_field(x, sort_field) if '.' in sort_field or '[' in sort_field else x.get(sort_field)
			return (v is None, v)
		return sorted(recs, key=keyfn, reverse=reverse)

	def backupChanges(self, path: Optional[str], old_data, new_data):
		"""Explicit backup call (not required if _maybe_backup is wired in)."""
		if not self.backups_enabled:
			return {"error": "Backups disabled"}
		self._maybe_backup(path or '', old_data)
		return {"success": "Backup created"}

	def recoverPath(self, path: Optional[str], timestamp: str, protect: Optional[List[str]] = None):
		"""
		Restore from backups: uses a timestamp string used in filenames (YYYYmmdd-HHMMSS).
		"""
		if not self.is_file_mode or not self.backups_enabled:
			return {"error": "Backups are disabled or not file-backed"}
		if not path:
			return {"error": "Path required for recoverPath"}

		backup_dir = os.path.join(self.backup_dir, path.replace('.', os.sep))
		target_file = os.path.join(backup_dir, f"{timestamp}.json")
		if not os.path.exists(target_file):
			return {"error": "Backup file not found"}

		with open(target_file, 'r', encoding='utf-8') as f:
			backup_data = json.load(f)

		if protect:
			current_data = copy.deepcopy(self._get_node(path))
			if current_data is not None:
				for dotted in protect:
					prot_val = self._get_field(current_data, dotted)
					if prot_val is not None:
						# Overlay protection into backup_data at dotted path
						self._set_field(backup_data, dotted, prot_val)

		self.overwriteEnd(path, json.dumps(backup_data))
		return {"success": f"Data recovered from {target_file}"}

	def mergeData(self, target: dict, newData: dict, overwriteIfExists: bool = True):
		"""Deep merge dicts; extend lists when both are lists."""
		for k, v in newData.items():
			if k in target:
				# lists first to avoid overwrite
				if isinstance(target[k], list) and isinstance(v, list):
					target[k].extend(v)
				elif isinstance(target[k], dict) and isinstance(v, dict):
					self.mergeData(target[k], v, overwriteIfExists)
				elif overwriteIfExists:
					target[k] = v
			else:
				target[k] = v

	def appendEnd(self, path: Optional[str], jsonData: str, overwriteIfExists: bool = True):
		"""
		Append to list at path. Creates list if missing.
		"""
		dataToInsert = json.loads(jsonData)
		# ensure a list exists
		parent, key, is_list = self._traverse(path, create=True, ensure_list_final=True)
		if parent is None and key is None:
			# root is the target
			if not isinstance(self.data, list):
				if overwriteIfExists:
					old = copy.deepcopy(self.data)
					self._maybe_backup('(root)', old)
					self.data = []
				else:
					return {"error": "Target is not a list and overwrite is not allowed"}
			if isinstance(dataToInsert, list):
				self.data.extend(dataToInsert)
			else:
				self.data.append(dataToInsert)
			self.index = self.indexJson(self.data)
			self._persist()
			return {"success": f"Data appended at root"}
		# normal non-root
		lst = parent[key]
		if not isinstance(lst, list):
			if overwriteIfExists:
				self._maybe_backup(path or '', copy.deepcopy(lst))
				parent[key] = []
				lst = parent[key]
			else:
				return {"error": "Target is not a list and overwrite is not allowed"}

		if isinstance(dataToInsert, list):
			lst.extend(dataToInsert)
		else:
			lst.append(dataToInsert)
		self.index = self.indexJson(self.data)
		self._persist()
		return {"success": f"Data appended at {path}"}

	def recoverRollback(self, timestamp: str, protect: Optional[List[str]] = None):
		"""
		Roll back all paths that have a backup at the given timestamp.
		"""
		if (not self.is_file_mode) or (not self.backups_enabled):
			return {"error": "Backups are disabled or not file-backed"}

		pattern = os.path.join(self.backup_dir, "**", f"{timestamp}.json")
		backup_files = glob.glob(pattern, recursive=True)
		if not backup_files:
			return {"error": "No backups found for the given timestamp"}

		for bf in backup_files:
			rel = os.path.relpath(bf, self.backup_dir)
			dirname = os.path.dirname(rel)
			dotted = dirname.replace(os.sep, '.')
			self.recoverPath(dotted, timestamp, protect)

		return {"success": "Rollback completed successfully"}

	def insert(self, path: Optional[str], newData: Any):
		"""
		Insert a new record into list at path; creates list if missing.
		"""
		parent, key, _ = self._traverse(path, create=True, ensure_list_final=True)
		if parent is None and key is None:
			# root
			if not isinstance(self.data, list):
				self._maybe_backup('(root)', copy.deepcopy(self.data))
				self.data = []
			self.data.append(newData)
		else:
			lst = parent[key]
			if not isinstance(lst, list):
				return {"error": "Target is not a list, cannot insert"}
			lst.append(newData)
		self.index = self.indexJson(self.data)
		self._persist()
		return {"success": f"Data inserted at {path if path else 'root'}"}

	def insertMany(self, path: Optional[str], records: List[Any]):
		if not isinstance(records, list):
			return {"error": "Records must be a list"}
		parent, key, _ = self._traverse(path, create=True, ensure_list_final=True)
		if parent is None and key is None:
			if not isinstance(self.data, list):
				self._maybe_backup('(root)', copy.deepcopy(self.data))
				self.data = []
			self.data.extend(records)
		else:
			lst = parent[key]
			if not isinstance(lst, list):
				return {"error": "Target is not a list, cannot insert multiple records"}
			lst.extend(records)
		self.index = self.indexJson(self.data)
		self._persist()
		return {"success": f"{len(records)} records inserted at {path if path else 'root'}"}

	def insertChild(self, path: Optional[str], parentCondition, omitConditions, childField: str, childData: Any):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of parent records"}
		old = copy.deepcopy(records)
		modified = False
		for rec in records:
			if self.matchConditions(rec, parentCondition) and not self.matchConditions(rec, omitConditions):
				if childField not in rec or not isinstance(rec[childField], list):
					rec[childField] = []
				rec[childField].append(childData)
				modified = True
		if not modified:
			return {"error": "No matching parent records found for insertion"}
		self._maybe_backup(path or '', old)
		self.overwriteEnd(path, json.dumps(records))
		return {"success": "Child data inserted successfully"}

	def find(self, path: Optional[str], searchConditions=None, omitConditions=None):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}
		return [
			r for r in records
			if self.matchConditions(r, searchConditions) and not self.matchConditions(r, omitConditions)
		]

	def findOne(self, path: Optional[str], searchConditions=None, omitConditions=None):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}
		for r in records:
			if self.matchConditions(r, searchConditions) and not self.matchConditions(r, omitConditions):
				return r
		return None

	def updateNestedField(self, path: Optional[str], searchConditions, omitConditions, field: str, nestedUpdates: Any):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}
		old = copy.deepcopy(records)
		modified = False
		for r in records:
			if self.matchConditions(r, searchConditions) and not self.matchConditions(r, omitConditions):
				if field in r and isinstance(r[field], dict) and isinstance(nestedUpdates, dict):
					self.mergeData(r[field], nestedUpdates, overwriteIfExists=True)
				else:
					r[field] = nestedUpdates
				modified = True
		if not modified:
			return {"error": "No matching records found for update"}
		self._maybe_backup(path or '', old)
		self.overwriteEnd(path, json.dumps(records))
		return {"success": f"Nested field '{field}' updated successfully"}

	def deleteNestedField(self, path: Optional[str], searchConditions, omitConditions, nestedField: str):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}
		old = copy.deepcopy(records)
		modified = False
		for r in records:
			if self.matchConditions(r, searchConditions) and not self.matchConditions(r, omitConditions):
				if nestedField in r:
					del r[nestedField]
					modified = True
		if not modified:
			return {"error": "No matching records found for deletion"}
		self._maybe_backup(path or '', old)
		self.overwriteEnd(path, json.dumps(records))
		return {"success": f"Nested field '{nestedField}' deleted successfully"}

	# -------- Safe compute / expression eval --------

	def _safe_eval(self, expr: str, names: dict) -> Any:
		"""
		Safely evaluate arithmetic/boolean expressions using AST whitelist.
		Allowed: literals, names, +,-,*,/,//,%, **, unary +/-, comparisons, and/or/not, parentheses.
		"""
		node = ast.parse(expr, mode='eval')

		allowed = (
			ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant,
			ast.Name, ast.Load, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv,
			ast.Mod, ast.Pow, ast.USub, ast.UAdd, ast.Compare, ast.Eq, ast.NotEq,
			ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.BoolOp, ast.And, ast.Or, ast.Not
		)

		def _check(n):
			if not isinstance(n, allowed):
				raise ValueError(f"Disallowed expression: {type(n).__name__}")
			for child in ast.iter_child_nodes(n):
				_check(child)

		_check(node)

		# Build a safe locals namespace from names (record fields)
		safe_locals = {k: v for k, v in names.items() if isinstance(k, str)}
		return eval(compile(node, '<expr>', 'eval'), {"__builtins__": {}}, safe_locals)

	def computeField(self, path: Optional[str], operation: str, computeField: str,
					searchConditions=None, omitConditions=None):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}
		old = copy.deepcopy(records)
		modified = False
		for r in records:
			if self.matchConditions(r, searchConditions) and not self.matchConditions(r, omitConditions):
				try:
					r[computeField] = self._safe_eval(operation, r)
					modified = True
				except Exception as e:
					return {"error": f"Failed to compute field '{computeField}': {e}"}
		if not modified:
			return {"error": "No matching records found for computation"}
		self._maybe_backup(path or '', old)
		self.overwriteEnd(path, json.dumps(records))
		return {"success": f"Computed field '{computeField}' updated successfully"}

	# -------- Transactions --------

	def beginTransaction(self):
		if self.transaction_data is not None:
			return {"error": "Transaction already in progress"}
		self.transaction_data = json.loads(json.dumps(self.data))  # deep copy
		return {"success": "Transaction started"}

	def commit(self):
		if self.transaction_data is None:
			return {"error": "No active transaction to commit"}
		self.transaction_data = None
		self._persist()
		return {"success": "Transaction committed"}

	def rollback(self):
		if self.transaction_data is None:
			return {"error": "No active transaction to roll back"}
		self.data = self.transaction_data
		self.transaction_data = None
		self.index = self.indexJson(self.data)
		return {"success": "Transaction rolled back"}

	# -------- Child deletions & bulk ops --------

	def deleteChild(self, path: Optional[str], parentCondition, omitConditions, childField: str, childCondition):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of parent records"}
		old = copy.deepcopy(records)
		modified = False
		for parent in records:
			if self.matchConditions(parent, parentCondition) and not self.matchConditions(parent, omitConditions):
				if childField in parent and isinstance(parent[childField], list):
					before = len(parent[childField])
					parent[childField] = [
						c for c in parent[childField] if not self.matchConditions(c, childCondition)
					]
					if len(parent[childField]) != before:
						modified = True
		if not modified:
			return {"error": "No matching child records found for deletion"}
		self._maybe_backup(path or '', old)
		self.overwriteEnd(path, json.dumps(records))
		return {"success": f"Child records deleted from '{childField}'"}

	def findLimited(self, path: Optional[str], searchConditions=None, omitConditions=None,
					limit: int = 10, offset: int = 0):
		records = self.find(path, searchConditions, omitConditions)
		if isinstance(records, dict) and "error" in records:
			return records
		return records[offset: offset + limit]

	def updateMany(self, path: Optional[str], searchConditions=None, omitConditions=None, updates: Optional[dict] = None):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}
		if not updates or not isinstance(updates, dict):
			return {"error": "Updates must be a valid dictionary"}
		old = copy.deepcopy(records)
		modified = False
		for r in records:
			if self.matchConditions(r, searchConditions) and not self.matchConditions(r, omitConditions):
				for k, v in updates.items():
					r[k] = v
				modified = True
		if not modified:
			return {"error": "No records matched update conditions"}
		self._maybe_backup(path or '', old)
		self.overwriteEnd(path, json.dumps(records))
		return {"success": "Records updated successfully"}

	def findRegex(self, path: Optional[str], field: str, pattern: str):
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "No records found at path: " + str(path)}
		try:
			rx = re.compile(pattern)
		except re.error as e:
			return {"error": f"Invalid regex: {e}"}
		out = []
		for r in records:
			v = self._get_field(r, field) if ('.' in field or '[' in field) else r.get(field)
			if isinstance(v, str) and rx.search(v):
				out.append(r)
		return out

	def findProjected(self, path: Optional[str], search_conditions=None, omit_conditions=None, fields: Optional[List[str]] = None):
		recs = self.find(path, search_conditions, omit_conditions)
		if isinstance(recs, dict) and "error" in recs:
			return recs
		if not fields:
			return recs
		proj = []
		for r in recs:
			proj.append({f: self._get_field(r, f) if ('.' in f or '[' in f) else r.get(f) for f in fields if f})
		return proj

	def navigateOrCreate(self, path: Optional[str]):
		"""Ensure path exists; return the dict/list node at path."""
		parent, key, _ = self._traverse(path, create=True)
		if parent is None and key is None:
			return self.data
		return parent[key]

	def mergePathProtected(self, path: Optional[str], backupData: dict, protect: List[str]):
		self.index = self.indexJson(self.data)
		# Ensure target path is dict; if leaf or missing, convert to dict
		parent, key, _ = self._traverse(path, create=True)
		if parent is None and key is None:
			if not isinstance(self.data, dict):
				# convert root to dict
				self.data = {}
			target = self.data
		else:
			if not isinstance(parent[key], dict):
				parent[key] = {}
			target = parent[key]
		self.mergeProtected(backupData, target, protect, prefix="")
		self.index = self.indexJson(self.data)
		self._persist()
		return {"success": f"Merged data into path '{path}', respecting protected fields."}

	def mergeProtected(self, backup: Any, current: Any, protect: List[str], prefix: str = ""):
		if not isinstance(backup, dict) or not isinstance(current, dict):
			# overwrite unless path is protected
			return current if prefix in protect else backup
		for k, v in backup.items():
			full = f"{prefix}.{k}" if prefix else k
			if full in protect:
				continue
			if k in current and isinstance(current[k], dict) and isinstance(v, dict):
				current[k] = self.mergeProtected(v, current[k], protect, full)
			else:
				current[k] = self.mergeProtected(v, current.get(k), protect, full)
		return current

	def findDifferences(self, oldData: Any, newData: Any, path: str = "") -> Dict[str, dict]:
		diffs = {}
		if isinstance(oldData, dict) and isinstance(newData, dict):
			old_keys = set(oldData.keys())
			new_keys = set(newData.keys())
			for k in old_keys - new_keys:
				p = f"{path}.{k}" if path else k
				diffs[p] = {"removed": oldData[k]}
			for k in new_keys - old_keys:
				p = f"{path}.{k}" if path else k
				diffs[p] = {"added": newData[k]}
			for k in old_keys & new_keys:
				p = f"{path}.{k}" if path else k
				diffs.update(self.findDifferences(oldData[k], newData[k], p))
		elif isinstance(oldData, list) and isinstance(newData, list):
			# Compare lists by index
			maxlen = max(len(oldData), len(newData))
			for i in range(maxlen):
				p = f"{path}[{i}]" if path else f"[{i}]"
				ov = oldData[i] if i < len(oldData) else "__MISSING__"
				nv = newData[i] if i < len(newData) else "__MISSING__"
				if ov == "__MISSING__":
					diffs[p] = {"added": nv}
				elif nv == "__MISSING__":
					diffs[p] = {"removed": ov}
				elif isinstance(ov, (dict, list)) and isinstance(nv, type(ov)):
					diffs.update(self.findDifferences(ov, nv, p))
				elif ov != nv:
					diffs[p] = {"changed": {"old": ov, "new": nv}}
		else:
			if oldData != newData:
				diffs[path] = {"changed": {"old": oldData, "new": newData}}
		return diffs

	def getJson(self):
		return json.dumps(self.data, indent=4)

	# ---------------------------
	# Small helpers
	# ---------------------------

	def _parent_path(self, path: Optional[str]) -> Optional[str]:
		if not path:
			return None
		spec = self._parse_path(path)
		if not spec:
			return None
		# render spec except the last step
		render = self._render_spec(spec[:-1])
		return render

	def _render_spec(self, spec: List[Tuple[Optional[str], Optional[int]]]) -> str:
		parts = []
		for key, idx in spec:
			if key is not None:
				parts.append(key.replace('.', '\\.'))
			if idx is not None:
				if not parts:
					parts.append(f"[{idx}]")
				else:
					parts[-1] += f"[{idx}]"
		return '.'.join(parts)

	def _set_field(self, root: Any, dotted: str, value: Any):
		spec = self._parse_path(dotted)
		if not spec:
			# replace root
			self.data = value
			return
		cur = root
		for i, (key, idx) in enumerate(spec):
			is_last = (i == len(spec) - 1)
			if key is not None:
				if not isinstance(cur, dict):
					raise ValueError(f"Cannot set {dotted}: expected dict at {key}")
				if key not in cur:
					cur[key] = [] if idx is not None else ({} if not is_last else value)
				if is_last and idx is None:
					cur[key] = value
					return
				cur = cur[key]
			if idx is not None:
				if not isinstance(cur, list):
					raise ValueError(f"Cannot set {dotted}: expected list at index {idx}")
				while idx >= len(cur):
					cur.append({} if not is_last else value)
				if is_last:
					cur[idx] = value
					return
				cur = cur[idx]

	# ---------------------------
	# (Optional) Rule-engine hooks
	# ---------------------------

	def applyRules(self, path: Optional[str], rules: List[dict]) -> dict:
		"""
		Apply a list of rules to records at `path`. Each rule:
		{
			"when": { ...conditions... },
			"omit": { ...conditions... },        # optional
			"then": [
				{"set": {"field": "a.b", "value": 1}},
				{"delete": {"field": "c"}},
				{"compute": {"field": "score", "expr": "price * qty"}},
			]
		}
		"""
		records = self._get_node(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}

		old = copy.deepcopy(records)
		count = 0
		for r in records:
			for rule in rules:
				when = rule.get("when")
				omit = rule.get("omit")
				if self.matchConditions(r, when) and not self.matchConditions(r, omit):
					for action in rule.get("then", []):
						if "set" in action:
							fld = action["set"]["field"]
							val = action["set"]["value"]
							self._set_field(r, fld, val)
							count += 1
						elif "delete" in action:
							fld = action["delete"]["field"]
							self._delete_field(r, fld)
							count += 1
						elif "compute" in action:
							fld = action["compute"]["field"]
							expr = action["compute"]["expr"]
							val = self._safe_eval(expr, r)
							self._set_field(r, fld, val)
							count += 1
		if count:
			self._maybe_backup(path or '', old)
			self.overwriteEnd(path, json.dumps(records))
		return {"success": f"Rules applied: {count} actions"}

	def _delete_field(self, root: Any, dotted: str):
		spec = self._parse_path(dotted)
		if not spec:
			return
		# Traverse to parent of last
		cur = root
		for i, (key, idx) in enumerate(spec):
			is_last = (i == len(spec) - 1)
			if key is not None:
				if not isinstance(cur, dict) or key not in cur:
					return
				if is_last and idx is None:
					del cur[key]
					return
				cur = cur[key]
			if idx is not None:
				if not isinstance(cur, list) or idx >= len(cur):
					return
				if is_last:
					del cur[idx]
					return
				cur = cur[idx]