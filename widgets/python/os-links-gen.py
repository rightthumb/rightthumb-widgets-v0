import os

def find_links_recursive(start_dir):
    inodes_seen = {}  # A dictionary to track inodes we've seen

    for root, dirs, files in os.walk(start_dir):
        for name in dirs + files:  # Loop over files and directories
            full_path = os.path.join(root, name)

            # Check if it's a symbolic link
            if os.path.islink(full_path):
                source = os.readlink(full_path)  # Find source of symbolic link
                print(f"ln -s {source} {full_path}")
                continue  # Skip further checks for symbolic links
            
            # Now check for hard links
            try:
                stat_info = os.stat(full_path)  # Get file stats
            except FileNotFoundError:
                continue

            inode = stat_info.st_ino  # Get inode number
            
            # If we've seen this inode before, it's a hard link
            if inode in inodes_seen:
                # For hard links, the concept of source is ambiguous
                # So, not generating an ln command for hard links
                pass
            else:
                inodes_seen[inode] = full_path  # Save the inode

if __name__ == "__main__":
    start_dir = "."  # Replace this with the path where you want to start the search
    find_links_recursive(start_dir)
