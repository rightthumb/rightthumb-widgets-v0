import os
import sys


# List of extensions to ignore
IGNORE_EXTENSIONS = [
	".zip", ".tar", ".tar.gz", ".tar.bz2", ".gz", ".bz2", ".rar", ".xz",
	".tar.xz", ".7z", ".zst", ".lzma", ".lz4", ".lzh", ".cab", ".ace",
	".tar.Z", ".tar.lz", ".tar.lzma", ".tar.lzo", ".tar.lrz", ".tar.lzop"
]

def should_ignore_file(filename):
	# Check if the file has one of the specified extensions
	return any(filename.endswith(ext) for ext in IGNORE_EXTENSIONS)


def find_second_file_folder(root_dir, count=[0]):
	# List the contents of the current directory
	for entry in os.listdir(root_dir):
		# Construct the full path of the entry
		entry_path = os.path.join(root_dir, entry)
		# If the entry is a file, check the count and return the current directory if necessary
		if os.path.isfile(entry_path):
			if not should_ignore_file(entry_path):
				return root_dir
			count[0] += 1
			if count[0] == 2:
				return root_dir
		# If the entry is a directory, recurse into it
		elif os.path.isdir(entry_path):
			result = find_second_file_folder(entry_path, count)
			# If the second folder containing a file is found, return its path
			if result is not None:
				return result
	# If no files are found in the current directory or its subdirectories, return None
	return None

if __name__ == "__main__":
	# Check if the user provided the root directory as a command-line argument
	if len(sys.argv) != 2:
		print("Usage: python3 locateDecompressedFiles.py <root_directory>")
		sys.exit(1)

	# Get the root directory from the command-line argument
	root_directory = sys.argv[1]

	# Find the second folder containing a file
	folder_with_file = find_second_file_folder(root_directory)

	# Print the result
	if folder_with_file is not None:
		print(folder_with_file)
		# print(f"The second folder containing a file is: {folder_with_file}")
	# else:
		# print("No second folder containing a file was found in the specified directory or its subdirectories.")