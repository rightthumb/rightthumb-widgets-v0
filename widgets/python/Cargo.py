import os
import time
from shutil import move

def create_cargo_toml():
	cargo_toml_path = 'Cargo.toml'
	
	# Check if Cargo.toml already exists
	if os.path.exists(cargo_toml_path):
		# Get the current timestamp (epoch)
		modification_epoch = str(int(time.time()))
		
		# Rename the existing Cargo.toml
		new_name = f'Cargo-{modification_epoch}.toml'
		move(cargo_toml_path, new_name)
		print(f'Renamed existing Cargo.toml to {new_name}')
	
	# Create a generic Cargo.toml file
	cargo_toml_content = """[package]
name = "my_project"
version = "0.1.0"
authors = ["Scott Reph <Scott@SoftwareDevelopmentSolutionsLLC.com>"]
edition = "2021"

[dependencies]
"""
	
	with open(cargo_toml_path, 'w') as file:
		file.write(cargo_toml_content)
	
	print(f'Created new {cargo_toml_path} file')

if __name__ == '__main__':
	create_cargo_toml()