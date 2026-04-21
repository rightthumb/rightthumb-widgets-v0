# markdown_printer.py

from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich import box

console = Console()

class MarkdownPrinter:

    def __init__(self, cfg=None):
        self.cfg = cfg or {
            "theme": "default",
            "table_style": "cyan",
            "header_style": "bold magenta",
            "border_style": "dim",
        }

    def print_markdown(self, cfg):
        """
        Print markdown with rich formatting

        cfg:
            text: markdown string
        """
        text = cfg.get("text", "")
        md = Markdown(text)
        console.print(md)

    def print_table(self, cfg):
        """
        Print table directly (bypasses markdown if needed)

        cfg:
            headers: []
            rows: []
            title: optional
        """
        headers = cfg.get("headers", [])
        rows = cfg.get("rows", [])
        title = cfg.get("title")

        table = Table(
            title=title,
            box=box.ROUNDED,
            header_style=self.cfg.get("header_style"),
            border_style=self.cfg.get("border_style"),
        )

        for h in headers:
            table.add_column(str(h))

        for row in rows:
            table.add_row(*[str(x) for x in row])

        console.print(table)

    def print_blocks(self, cfg):
        """
        Future-friendly:
        print your normalized block structure

        cfg:
            blocks: list of blocks
        """
        blocks = cfg.get("blocks", [])

        for block in blocks:
            t = block.get("type")

            if t == "heading":
                level = block.get("level", 1)
                text = block.get("text", "")
                console.print(f"{'#' * level} {text}", style="bold")

            elif t == "paragraph":
                console.print(block.get("text", ""))

            elif t == "table":
                self.print_table({
                    "headers": block.get("headers", []),
                    "rows": block.get("rows", []),
                    "title": " > ".join(block.get("path", []))
                })

            elif t == "list_item":
                console.print(f"- {block.get('text','')}")

            elif t == "link":
                console.print(f"[link={block.get('href')}]{block.get('text')}[/link]")

            console.print("")  # spacing``