#!/usr/bin/env python3

import sys
from collections import defaultdict

def count_duplicates(lines, strip=True):
	counts = defaultdict(int)

	for line in lines:
		if strip:
			line = line.strip()
		counts[line] += 1

	# Build sorted result table (least to most common)
	table = sorted(
		[{'line': line, 'count': count} for line, count in counts.items()],
		key=lambda x: x['count']
	)

	# Print table
	for row in table:
		print(f"{row['count']:>4}  {row['line']}")

	print()
	print(f"Groups of duplicates: {len(table)}")
	print(f"Total items: {sum(row['count'] for row in table)}")

def main():
	# Only run if there's piped input
	if sys.stdin.isatty():
		print("Usage: cat file.txt | python count_dupes.py")
		sys.exit(1)

	lines = sys.stdin.readlines()
	count_duplicates(lines, strip=True)

if __name__ == '__main__':
	main()