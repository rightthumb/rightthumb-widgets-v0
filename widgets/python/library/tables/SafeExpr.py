from typing import Any, Dict, List, Optional, Tuple
import re, math
from datetime import datetime, date

Row = Dict[str, Any]


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