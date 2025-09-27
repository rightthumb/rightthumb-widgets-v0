from typing import Any, Dict, List, Optional, Tuple
import re, math
from datetime import datetime, date

Row = Dict[str, Any]



# Registration: 6896754b-a824-832c-8c0b-b7d351d80325


class TableTool:
	def __init__(self, rows: List[Row]):
		self.rows: List[Row] = rows
		self.field_triggers: Dict[str, List[Dict[str, Any]]] = {}
		self.row_triggers: List[Dict[str, Any]] = []
		self.logs: List[str] = []
		# NEW: registries
		self.custom_field_ops: Dict[str, Any] = {}
		self.custom_row_funcs: Dict[str, Any] = {}

	# ---- NEW: register custom callables ----
	def register_field_op(self, name: str, fn):
		"""Register a custom field operation: fn(value, row, **params) -> new_value"""
		self.custom_field_ops[name] = fn
		self.logs.append(f"register_field_op: {name}")

	def register_row_func(self, name: str, fn):
		"""Register a custom row function: fn(row, **params) -> (dict | any)"""
		self.custom_row_funcs[name] = fn
		self.logs.append(f"register_row_func: {name}")

	def add_row_func(self, fn_or_name, target: Optional[str] = None, **params):
		"""
		Add a row-level function trigger.
		If target is provided, assign return value to that field.
		If no target and function returns dict, row.update(returned_dict).
		"""
		self.row_triggers.append({"type": "func", "fn": fn_or_name, "target": target, "params": params})
		self.logs.append(f"row_func: target={target} fn={fn_or_name} params={params}")

	# ---- field ops ----
	def _apply_op(self, value, row: Row, op: str, params: Dict[str, Any]):
		# NEW: support named custom ops directly
		if op in self.custom_field_ops:
			fn = self.custom_field_ops[op]
			return fn(value, row, **params)

		# NEW: generic function op
		if op == "func":
			fn = params.get("fn")
			extra = {k: v for k, v in params.items() if k != "fn"}
			if isinstance(fn, str):
				if fn not in self.custom_field_ops:
					raise KeyError(f"Unknown field op: {fn}")
				fn = self.custom_field_ops[fn]
			if not callable(fn):
				raise TypeError("field func must be callable or registered name")
			return fn(value, row, **extra)

		# ... (keep built-ins below unchanged)
		if op == "default":
			return value if value not in (None, "") else params.get("value")
		if op == "strip":
			return value.strip() if isinstance(value, str) else value
		if op == "lower":
			return value.lower() if isinstance(value, str) else value
		if op == "upper":
			return value.upper() if isinstance(value, str) else value
		if op == "title":
			return value.title() if isinstance(value, str) else value
		if op == "replace":
			if isinstance(value, str):
				return value.replace(params.get("old", ""), params.get("new", ""))
			return value
		if op == "regex_extract":
			if not isinstance(value, str):
				return params.get("default")
			m = re.search(params.get("pattern", ""), value, re.I | re.M)
			if not m:
				return params.get("default")
			g = params.get("group", 0)
			return m.group(g) if m.groups() or g == 0 else params.get("default")
		if op == "map":
			mapping = params.get("mapping", {})
			return mapping.get(value, params.get("default", value))
		if op == "coalesce":
			for key in params.get("fields", []):
				v = row.get(key)
				if v not in (None, ""):
					return v
			return value
		if op == "cast":
			typ = params.get("type")
			try:
				if typ in ("int", int): return int(value)
				if typ in ("float", float): return float(value)
				if typ in ("str", str): return str(value)
				if typ in ("bool", bool): return bool(value)
			except Exception:
				return None
			return value
		if op == "round":
			try:
				return round(float(value), params.get("ndigits", 0))
			except Exception:
				return value
		if op == "expr":
			expr = SafeExpr(params.get("expr", ""))
			names = dict(row); names["_"] = value
			return expr.eval(names)

		return value

	# ---- pipeline ----
	def run_triggers(self):
		for row in self.rows:
			# per-field
			for field, ops in self.field_triggers.items():
				cur = row.get(field)
				for spec in ops:
					op = spec["op"]
					params = {k: v for k, v in spec.items() if k != "op"}
					cur = self._apply_op(cur, row, op, params)
				row[field] = cur
			# per-row
			for rt in self.row_triggers:
				if rt.get("type") == "func":
					fn = rt["fn"]
					params = rt.get("params", {})
					if isinstance(fn, str):
						if fn not in self.custom_row_funcs:
							raise KeyError(f"Unknown row func: {fn}")
						fn = self.custom_row_funcs[fn]
					result = fn(row, **params)
					if rt.get("target") is not None:
						row[rt["target"]] = result
					else:
						if isinstance(result, dict):
							row.update(result)
				else:
					# default expr row trigger
					row[rt["target"]] = SafeExpr(rt["expr"]).eval(row)

	# ---- aggregates ----
	def aggregate(self, spec: Dict[str, Any]) -> List[Row]:
		rows = self.filter_rows(spec.get("filter"))
		gb = spec.get("group_by", [])
		groups: Dict[Tuple, List[Row]] = {}
		for r in rows:
			key = tuple(r.get(k) for k in gb) if gb else ("__all__",)
			groups.setdefault(key, []).append(r)

		def apply_metric(rs: List[Row], metric: Dict[str, Any]):
			if "sum" in metric:
				f = metric["sum"]; return sum(float(x.get(f, 0) or 0) for x in rs)
			if "mean" in metric:
				f = metric["mean"]; vals = [float(x.get(f, 0) or 0) for x in rs]
				return (sum(vals) / len(vals)) if vals else None
			if "min" in metric:
				f = metric["min"]; vals = [x.get(f) for x in rs if x.get(f) is not None]
				return min(vals) if vals else None
			if "max" in metric:
				f = metric["max"]; vals = [x.get(f) for x in rs if x.get(f) is not None]
				return max(vals) if vals else None
			if "count" in metric:
				return len(rs)
			if "nunique" in metric:
				f = metric["nunique"]; return len({x.get(f) for x in rs})
			if "expr" in metric:
				return SafeExpr(metric["expr"]).eval({"rows": rs, "len": len(rs)})
			# NEW: function metric
			if "func" in metric:
				fn = metric["func"]
				if isinstance(fn, str):
					# reuse row func registry for aggregates too
					if fn not in self.custom_row_funcs:
						raise KeyError(f"Unknown metric func: {fn}")
					fn = self.custom_row_funcs[fn]
				if not callable(fn):
					raise TypeError("aggregate func must be callable or registered name")
				return fn(rs)
			return None

		out: List[Row] = []
		for key, rs in groups.items():
			rec: Row = {}
			for i, kf in enumerate(gb):
				rec[kf] = key[i]
			for name, metric in spec.get("metrics", {}).items():
				rec[name] = apply_metric(rs, metric)
			out.append(rec)
		return out






class SafeExpr:
	"""
	Safe-ish expression evaluator for formulas on a row dict.

	Allowed:
	- literals, names passed in, whitelisted builtins/types
	- arithmetic: + - * / // % **
	- comparisons: < <= > >= == != in not in
	- boolean: and, or, not
	- attribute access (e.g., math.isnan), indexing/slicing, ternary (a if c else b)

	Use: SafeExpr("qty * price").eval(row)
	"""
	ALLOWED_NAMES = {
		# common builtins
		"abs": abs, "round": round, "len": len, "min": min, "max": max, "sum": sum,
		"any": any, "all": all,
		# types / helpers
		"isinstance": isinstance,
		"int": int, "float": float, "str": str, "bool": bool,
		"list": list, "dict": dict, "set": set, "tuple": tuple,
		# modules / constants
		"math": math,
		"True": True, "False": False, "None": None,
		"datetime": datetime, "date": date,
	}

	def __init__(self, expr: str):
		import ast
		self.expr = expr
		self.ast_mod = ast
		self.ast = ast.parse(expr, mode="eval").body

	def _eval(self, node, names):
		ast = self.ast_mod
		if isinstance(node, ast.Constant):
			return node.value

		if isinstance(node, ast.Name):
			if node.id in names:
				return names[node.id]
			if node.id in self.ALLOWED_NAMES:
				return self.ALLOWED_NAMES[node.id]
			raise NameError(f"Unknown name: {node.id}")

		if isinstance(node, ast.BinOp):
			left = self._eval(node.left, names); right = self._eval(node.right, names)
			import operator as optr
			ops = {
				"Add": optr.add, "Sub": optr.sub, "Mult": optr.mul, "Div": optr.truediv,
				"FloorDiv": optr.floordiv, "Mod": optr.mod, "Pow": optr.pow,
			}
			return ops[type(node.op).__name__](left, right)

		if isinstance(node, ast.UnaryOp):
			val = self._eval(node.operand, names)
			import operator as optr
			ops = {"USub": optr.neg, "UAdd": optr.pos, "Not": optr.not_}
			fn = ops.get(type(node.op).__name__)
			if not fn: raise ValueError(f"Unsupported unary op: {type(node.op).__name__}")
			return fn(val)

		if isinstance(node, ast.BoolOp):
			vals = [self._eval(v, names) for v in node.values]
			return all(vals) if isinstance(node.op, ast.And) else any(vals)

		if isinstance(node, ast.Compare):
			left = self._eval(node.left, names)
			import operator as optr
			cmps = {
				"Lt": optr.lt, "LtE": optr.le, "Gt": optr.gt, "GtE": optr.ge,
				"Eq": optr.eq, "NotEq": optr.ne, "In": lambda a, b: a in b,
				"NotIn": lambda a, b: a not in b,
			}
			for op, comp in zip(node.ops, node.comparators):
				right = self._eval(comp, names)
				if not cmps[type(op).__name__](left, right):
					return False
				left = right
			return True

		if isinstance(node, ast.Call):
			func = self._eval(node.func, names)
			args = [self._eval(a, names) for a in node.args]
			kwargs = {kw.arg: self._eval(kw.value, names) for kw in node.keywords}
			return func(*args, **kwargs)

		if isinstance(node, ast.IfExp):
			return self._eval(node.body if self._eval(node.test, names) else node.orelse, names)

		if isinstance(node, ast.Attribute):
			value = self._eval(node.value, names)
			return getattr(value, node.attr)

		if isinstance(node, ast.List):
			return [self._eval(elt, names) for elt in node.elts]

		if isinstance(node, ast.Tuple):
			return tuple(self._eval(elt, names) for elt in node.elts)

		if isinstance(node, ast.Dict):
			return {self._eval(k, names): self._eval(v, names) for k, v in zip(node.keys, node.values)}

		if isinstance(node, ast.Subscript):
			value = self._eval(node.value, names)
			sl = node.slice
			if isinstance(sl, ast.Slice):
				lower = self._eval(sl.lower, names) if sl.lower else None
				upper = self._eval(sl.upper, names) if sl.upper else None
				step = self._eval(sl.step, names) if sl.step else None
				return value[lower:upper:step]
			key = self._eval(sl, names)
			return value[key]

		raise ValueError(f"Unsupported syntax node: {type(node)}")

	def eval(self, names: Dict[str, Any]):
		return self._eval(self.ast, names)
	


# "_.strip() if isinstance(_, str) else _"

# "qty * price if price and qty else 0"












'''


## Example: plug in your own functions

tool = TableTool(rows)

# FIELD FUNCTION: normalize SKU pieces
def squeeze_sku(value, row, keep_dash=True):
	if not isinstance(value, str): return value
	v = re.sub(r"[^A-Za-z0-9\-]+", "", value)
	return v.upper() if keep_dash else v.replace("-", "").upper()

tool.register_field_op("squeeze_sku", squeeze_sku)
tool.add_field_trigger("sku", "squeeze_sku", keep_dash=True)

# ROW FUNCTION: compute margin and maybe flag it
def compute_margin(row, fee_rate=0.03):
	price = float(row.get("price") or 0)
	qty   = int(row.get("qty") or 0)
	cost  = float(row.get("cost") or 0)
	rev   = price * qty
	fees  = rev * fee_rate
	margin = rev - cost*qty - fees
	# Return dict to update row in-place
	return {"revenue": rev, "fees": fees, "margin": margin, "profitable": margin >= 0}

tool.register_row_func("compute_margin", compute_margin)
tool.add_row_func("compute_margin", fee_rate=0.025)   # no target -> update dict

# Or compute and assign to a single field
def sku_prefix(row):
	sku = row.get("sku") or ""
	return sku.split("-")[0] if "-" in sku else sku

tool.add_row_func(sku_prefix, target="sku_prefix")

tool.run_triggers()






### Custom aggregate metric

def p95_price(rows):
	vals = sorted(float(r.get("price") or 0) for r in rows)
	if not vals: return None
	k = int(round(0.95*(len(vals)-1)))
	return vals[k]

tool.register_row_func("p95_price", p95_price)  # reuse same registry
aggs = tool.aggregate({
	"group_by": ["region"],
	"metrics": {
		"rows": {"count": "*"},
		"p95_price": {"func": "p95_price"},  # <- custom
	}
})



'''
















class SafeExpr:
	"""
	Safe-ish expression evaluator for formulas on a row dict.

	Allowed:
	- literals, names passed in, whitelisted builtins/types
	- arithmetic: + - * / // % **
	- comparisons: < <= > >= == != in not in
	- boolean: and, or, not
	- attribute access (e.g., math.isnan), indexing/slicing, ternary (a if c else b)

	Use: SafeExpr("qty * price").eval(row)
	"""
	ALLOWED_NAMES = {
		# common builtins
		"abs": abs, "round": round, "len": len, "min": min, "max": max, "sum": sum,
		"any": any, "all": all,
		# types / helpers
		"isinstance": isinstance,
		"int": int, "float": float, "str": str, "bool": bool,
		"list": list, "dict": dict, "set": set, "tuple": tuple,
		# modules / constants
		"math": math,
		"True": True, "False": False, "None": None,
		"datetime": datetime, "date": date,
	}

	def __init__(self, expr: str):
		import ast
		self.expr = expr
		self.ast_mod = ast
		self.ast = ast.parse(expr, mode="eval").body

	def _eval(self, node, names):
		ast = self.ast_mod
		if isinstance(node, ast.Constant):
			return node.value

		if isinstance(node, ast.Name):
			if node.id in names:
				return names[node.id]
			if node.id in self.ALLOWED_NAMES:
				return self.ALLOWED_NAMES[node.id]
			raise NameError(f"Unknown name: {node.id}")

		if isinstance(node, ast.BinOp):
			left = self._eval(node.left, names); right = self._eval(node.right, names)
			import operator as optr
			ops = {
				"Add": optr.add, "Sub": optr.sub, "Mult": optr.mul, "Div": optr.truediv,
				"FloorDiv": optr.floordiv, "Mod": optr.mod, "Pow": optr.pow,
			}
			return ops[type(node.op).__name__](left, right)

		if isinstance(node, ast.UnaryOp):
			val = self._eval(node.operand, names)
			import operator as optr
			ops = {"USub": optr.neg, "UAdd": optr.pos, "Not": optr.not_}
			fn = ops.get(type(node.op).__name__)
			if not fn: raise ValueError(f"Unsupported unary op: {type(node.op).__name__}")
			return fn(val)

		if isinstance(node, ast.BoolOp):
			vals = [self._eval(v, names) for v in node.values]
			return all(vals) if isinstance(node.op, ast.And) else any(vals)

		if isinstance(node, ast.Compare):
			left = self._eval(node.left, names)
			import operator as optr
			cmps = {
				"Lt": optr.lt, "LtE": optr.le, "Gt": optr.gt, "GtE": optr.ge,
				"Eq": optr.eq, "NotEq": optr.ne, "In": lambda a, b: a in b,
				"NotIn": lambda a, b: a not in b,
			}
			for op, comp in zip(node.ops, node.comparators):
				right = self._eval(comp, names)
				if not cmps[type(op).__name__](left, right):
					return False
				left = right
			return True

		if isinstance(node, ast.Call):
			func = self._eval(node.func, names)
			args = [self._eval(a, names) for a in node.args]
			kwargs = {kw.arg: self._eval(kw.value, names) for kw in node.keywords}
			return func(*args, **kwargs)

		if isinstance(node, ast.IfExp):
			return self._eval(node.body if self._eval(node.test, names) else node.orelse, names)

		if isinstance(node, ast.Attribute):
			value = self._eval(node.value, names)
			return getattr(value, node.attr)

		if isinstance(node, ast.List):
			return [self._eval(elt, names) for elt in node.elts]

		if isinstance(node, ast.Tuple):
			return tuple(self._eval(elt, names) for elt in node.elts)

		if isinstance(node, ast.Dict):
			return {self._eval(k, names): self._eval(v, names) for k, v in zip(node.keys, node.values)}

		if isinstance(node, ast.Subscript):
			value = self._eval(node.value, names)
			sl = node.slice
			if isinstance(sl, ast.Slice):
				lower = self._eval(sl.lower, names) if sl.lower else None
				upper = self._eval(sl.upper, names) if sl.upper else None
				step = self._eval(sl.step, names) if sl.step else None
				return value[lower:upper:step]
			key = self._eval(sl, names)
			return value[key]

		raise ValueError(f"Unsupported syntax node: {type(node)}")

	def eval(self, names: Dict[str, Any]):
		return self._eval(self.ast, names)
	

# 6896754b-a824-832c-8c0b-b7d351d80325