import sys
import re

class CodeMerger:
	def __init__(self, filename):
		self.filename = filename
		self.contents = self.read_file()
		self.language = self.detect_language()

	def read_file(self):
		"""Read the contents of the file."""
		try:
			with open(self.filename, 'r') as file:
				return file.read()
		except FileNotFoundError:
			raise FileNotFoundError(f"File {self.filename} not found.")

	def detect_language(self):
		"""Detect the programming language of the file based on its contents."""
		contents = self.contents
		if 'def ' in contents and 'class ' in contents:
			return 'Python'
		elif 'function ' in contents and 'class ' in contents:
			return 'JavaScript'
		elif 'public class ' in contents:
			return 'Java'
		elif 'fn ' in contents and 'struct ' in contents:
			return 'Rust'
		else:
			return 'Unknown language'

	def merge_code(self, new_code):
		"""Merge new code into the file if it matches existing structures."""
		if self.language == 'Python':
			# Simple Python code merging example:
			class_pattern = re.compile(r'class (\w+)')
			existing_classes = class_pattern.findall(self.contents)
			new_classes = class_pattern.findall(new_code)

			for new_class in new_classes:
				if new_class in existing_classes:
					# Assume new_code is well formatted and appending at the end of the class definition
					self.contents += f'\n{new_code}'
					self.save_changes()
					return "Code merged successfully."
			return "No matching class found for merging."

	def save_changes(self):
		"""Save the changes back to the file."""
		with open(self.filename, 'w') as file:
			file.write(self.contents)

	def get_language(self):
		"""Return the detected language."""
		return self.language


def main():
	if len(sys.argv) < 2:
		print("Usage: python script.py <filename>")
		sys.exit(1)

	filename = sys.argv[1]
	merger = CodeMerger(filename)

	print(f"Detected language: {merger.get_language()}")

	# Read additional code from stdin if piped
	if not sys.stdin.isatty():
		new_code = sys.stdin.read()
		result = merger.merge_code(new_code)
		print(result)

if __name__ == "__main__":
	main()