import sys
import os

def main():
	if sys.stdin.isatty():
		print("No piped input detected. Example usage:\n  echo command | python stream_exec.py")
		return

	command_str = sys.stdin.read().strip()
	if not command_str:
		print("No command received.")
		return

	print(f"\n[Executing]: {command_str}\n{'='*40}")
	rc = os.system(command_str)
	print(f"\n[Exit code]: {rc}\n{'='*40}")

if __name__ == '__main__':
	main()