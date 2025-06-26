class TableGenerator:
    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            raise ValueError("Input should be a list of dictionaries.")
        self.data = data
        self.headers = self._extract_headers()

    def _extract_headers(self):
        headers = set()
        for row in self.data:
            headers.update(row.keys())
        return list(headers)

    def generate_plain_text(self):
        """Generates a plain text table."""
        headers = self.headers
        rows = [headers] + [[str(row.get(h, "")) for h in headers] for row in self.data]

        # Calculate column widths
        col_widths = [max(len(str(item)) for item in col) for col in zip(*rows)]

        # Create table
        table = []
        for row in rows:
            table.append(" | ".join(f"{cell:<{col_widths[i]}}" for i, cell in enumerate(row)))

        # Add header separator
        separator = "-+-".join("-" * width for width in col_widths)
        table.insert(1, separator)

        return "\n".join(table)

    def generate_markdown(self):
        """Generates a Markdown table."""
        headers = self.headers
        rows = [[str(row.get(h, "")) for h in headers] for row in self.data]

        # Create header and separator
        header = "| " + " | ".join(headers) + " |"
        separator = "| " + " | ".join("---" for _ in headers) + " |"

        # Create data rows
        data_rows = ["| " + " | ".join(row) + " |" for row in rows]

        return "\n".join([header, separator] + data_rows)


# Example usage
if __name__ == "__main__":
    data = [
        {"Name": "Alice", "Age": 25, "City": "New York"},
        {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "City": "Chicago"},
    ]

    tg = TableGenerator(data)

    print("Plain Text Table:")
    print(tg.generate_plain_text())

    print("\nMarkdown Table:")
    print(tg.generate_markdown())
