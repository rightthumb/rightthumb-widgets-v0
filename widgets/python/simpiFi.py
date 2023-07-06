import os
import argparse

def find_files(folder, extension):
	for root, dirs, files in os.walk(folder):
		for file in files:
			if file.endswith(extension):
				yield os.path.relpath(os.path.join(root, file), folder)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-folder', required=True, help='Directory to search')
	args = parser.parse_args()

	folder = args.folder
	extension = '.md'
	
	for filepath in find_files(folder, extension):
		print(filepath)

if __name__ == "__main__":
	main()
