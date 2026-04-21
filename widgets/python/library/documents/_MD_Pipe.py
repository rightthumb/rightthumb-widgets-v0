#!/usr/bin/env python3

import sys
import re
from rich.console import Console
from rich.markup import escape

console = Console()

TOKENS = {
	"BOLD_OPEN":  "\x01BOLD_OPEN\x02",
	"BOLD_CLOSE": "\x01BOLD_CLOSE\x02",
	"ITALIC_OPEN":  "\x01ITALIC_OPEN\x02",
	"ITALIC_CLOSE": "\x01ITALIC_CLOSE\x02",
	"UNDER_OPEN": "\x01UNDER_OPEN\x02",
	"UNDER_CLOSE": "\x01UNDER_CLOSE\x02",
}

def transform(text: str) -> str:
	text = text.replace("\\\n", "\n")

	# combined styles first
	text = re.sub(
		r'\*\*\[([\s\S]+?)\]\{\.underline\}\*\*',
		TOKENS["BOLD_OPEN"] + TOKENS["UNDER_OPEN"] + r'\1' + TOKENS["UNDER_CLOSE"] + TOKENS["BOLD_CLOSE"],
		text
	)

	text = re.sub(
		r'\*\*\*([\s\S]+?)\*\*\*',
		TOKENS["BOLD_OPEN"] + TOKENS["ITALIC_OPEN"] + r'\1' + TOKENS["ITALIC_CLOSE"] + TOKENS["BOLD_CLOSE"],
		text
	)

	# single styles
	text = re.sub(
		r'\[([\s\S]+?)\]\{\.underline\}',
		TOKENS["UNDER_OPEN"] + r'\1' + TOKENS["UNDER_CLOSE"],
		text
	)

	text = re.sub(
		r'\*\*([\s\S]+?)\*\*',
		TOKENS["BOLD_OPEN"] + r'\1' + TOKENS["BOLD_CLOSE"],
		text
	)

	text = re.sub(
		r'(?<!\*)\*([^*\n][\s\S]*?)\*(?!\*)',
		TOKENS["ITALIC_OPEN"] + r'\1' + TOKENS["ITALIC_CLOSE"],
		text
	)

	# escape all document text so literal [ ] don't break Rich
	text = escape(text)

	# restore only our intentional Rich tags
	text = (
		text.replace(TOKENS["BOLD_OPEN"], "[bold]")
			.replace(TOKENS["BOLD_CLOSE"], "[/bold]")
			.replace(TOKENS["ITALIC_OPEN"], "[italic]")
			.replace(TOKENS["ITALIC_CLOSE"], "[/italic]")
			.replace(TOKENS["UNDER_OPEN"], "[u]")
			.replace(TOKENS["UNDER_CLOSE"], "[/u]")
	)

	return text

def main():
	data = sys.stdin.read()
	data = transform(data)
	console.print(data, markup=True)

if __name__ == "__main__":
	main()