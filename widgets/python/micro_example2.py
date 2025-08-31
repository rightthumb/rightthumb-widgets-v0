#!/usr/bin/python3

import os, sys
# Assuming the custom module is named underscore and contains the Underscore class

# Determine the root directory based on the OS platform
if sys.platform[0] == 'w': 
    _rt = os.getenv('USERPROFILE') + os.sep + '.rt' + os.sep
else:
    _rt = os.getenv('HOME') + os.sep + '.rt' + os.sep

app = _rt + 'micro.py'

# Properly open the file for reading and execute its content
try:
    with open(app, 'r') as file:
        exec(file.read())
except FileNotFoundError:
    print(f"Error: The file {app} does not exist.")
except Exception as e:
    print(f"An error occurred while executing {app}: {str(e)}")

# Example usage of the _ object
for path in _.fo():
    _.pr(path)
