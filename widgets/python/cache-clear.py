#!/usr/bin/python3
import os
import shutil
import traceback

def delete_pycaches(start_dir):
	for root, dirs, files in os.walk(start_dir):
		for dir in dirs:
			if dir == '__pycache__':
				pycache_path = os.path.join(root, dir)
				try:
					shutil.rmtree(pycache_path)
					print(f"Deleted: {pycache_path}")
				except Exception as e:
					print(f"Failed to delete {pycache_path}")
					print(traceback.format_exc())

def delete_pyc_files(start_dir):
	for root, dirs, files in os.walk(start_dir):
		for file in files:
			if file.endswith('.pyc'):
				pyc_file_path = os.path.join(root, file)
				try:
					os.remove(pyc_file_path)
					print(f"Deleted: {pyc_file_path}")
				except Exception as e:
					print(f"Failed to delete {pyc_file_path}")
					print(traceback.format_exc())

# REPLACE the entire `if __name__ == "__main__":` block with this

if __name__ == "__main__":
	import argparse
	import sys

	parser = argparse.ArgumentParser(
		description="Delete __pycache__ directories and .pyc files"
	)
	parser.add_argument(
		"-yes",
		action="store_true",
		help="Run cleanup immediately (no prompt)"
	)
	parser.add_argument(
		"path",
		nargs="?",
		default=".",
		help="Start directory (default: current directory)"
	)

	# If NO args at all → show help and exit
	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit(0)

	args = parser.parse_args()
	start_directory = args.path

	if not args.yes:
		print("Error: -yes is required to perform deletion.\n")
		parser.print_help()
		sys.exit(1)

	delete_pycaches(start_directory)
	delete_pyc_files(start_directory)
	print("Cleanup completed.")