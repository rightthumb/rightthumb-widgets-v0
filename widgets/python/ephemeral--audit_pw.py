#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


import os

def contains_target_strings(target_file, target_strings):
    """
    Check if the file contains any of the target strings.

    :param target_file: The path to the file to check.
    :param target_strings: The list of strings to search for.
    :return: True if any of the target strings are found in the file, False otherwise.
    """
    with open(target_file, 'r', errors='replace') as f:  # 'errors' param ensures it handles undecodable characters gracefully
        contents = f.read()
        for s in target_strings:
            if s in contents:
                return True
    return False

if __name__ == "__main__":
    # Modify these variables as needed
    target_strings = ['password1', 'password2', 'password3']  # Replace with your target strings

    # Iterate through all files in the current directory
    for filename in os.listdir('.'):
        if os.path.isfile(filename):  # Ensure it's a file, not a directory
            if contains_target_strings(filename, target_strings):
                print(filename)
