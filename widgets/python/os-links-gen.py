import os

def find_links_recursive(start_dir):
	inodes_seen = {}  # A dictionary to track inodes we've seen

	for root, dirs, files in os.walk(start_dir):
		for name in dirs + files:  # Loop over files and directories
			full_path = os.path.join(root, name)

			# Check if it's a symbolic link
			if os.path.islink(full_path):
				target = os.readlink(full_path)
				relative_link = os.path.relpath(full_path, start_dir)
				relative_target = os.path.relpath(target, start_dir)
				print(f"ln -s {relative_target} {relative_link}")
				continue  # Skip further checks for symbolic links
			
			# Now check for hard links
			try:
				stat_info = os.stat(full_path)  # Get file stats
			except FileNotFoundError:
				continue

			inode = stat_info.st_ino  # Get inode number
			
			# If we've seen this inode before, it's a hard link
			if inode in inodes_seen:
				relative_link = os.path.relpath(full_path, start_dir)
				relative_target = os.path.relpath(inodes_seen[inode], start_dir)
				print(f"ln {relative_target} {relative_link}")
			else:
				inodes_seen[inode] = full_path  # Save the inode

if __name__ == "__main__":
	start_dir = "."  # Replace this with the path where you want to start the search
	find_links_recursive(start_dir)