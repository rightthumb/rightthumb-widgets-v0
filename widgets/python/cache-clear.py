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

if __name__ == "__main__":
    start_directory = '.'  # You can set this to any directory you want to start from
    confirm = input(f"Are you sure you want to delete all __pycache__ directories and .pyc files in {start_directory}? (yes/no): ")
    if confirm.lower() == 'yes':
        delete_pycaches(start_directory)
        delete_pyc_files(start_directory)
        print("Cleanup completed.")
    else:
        print("Cleanup aborted.")
