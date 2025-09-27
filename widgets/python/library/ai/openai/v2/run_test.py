
# run_all_tests.py
import inspect
import sys
import traceback

def run_tests(module_name="test_gpt_client"):
	"""
	Import a test module, find all test_* functions, and run them.
	Prints results summary.
	"""
	try:
		mod = __import__(module_name)
	except ImportError as e:
		print(f"Could not import {module_name}: {e}")
		return

	funcs = [
		fn for name, fn in inspect.getmembers(mod, inspect.isfunction)
		if name.startswith("test_")
	]

	passed, failed = 0, 0
	for fn in funcs:
		try:
			fn()  # run with no args
			print(f"[PASS] {fn.__name__}")
			passed += 1
		except Exception:
			print(f"[FAIL] {fn.__name__}")
			traceback.print_exc(limit=3)
			failed += 1

	print("\n=== SUMMARY ===")
	print(f"Total: {len(funcs)}, Passed: {passed}, Failed: {failed}")


if __name__ == "__main__":
	# default to test_gpt_client but allow python run_all_tests.py other_module
	mod = sys.argv[1] if len(sys.argv) > 1 else "test_gpt_client"
	run_tests(mod)