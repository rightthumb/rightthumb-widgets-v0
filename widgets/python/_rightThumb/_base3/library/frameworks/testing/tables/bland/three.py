def generate_table(data):
    if not data:
        return "No data provided."

    # Extract headers
    headers = data[0].keys()

    # Determine column widths
    col_widths = {key: max(len(str(row[key])) for row in data) for key in headers}
    col_widths = {key: max(len(key), width) for key, width in col_widths.items()}

    # Create table header
    header_row = " | ".join(f"{key:<{col_widths[key]}}" for key in headers)
    separator = "-+-".join("-" * col_widths[key] for key in headers)

    # Create table rows
    rows = []
    for row in data:
        row_line = " | ".join(f"{str(row[key]):<{col_widths[key]}}" for key in headers)
        rows.append(row_line)

    # Combine header, separator, and rows
    table = "\n".join([header_row, separator] + rows)
    return table


# Example usage
if __name__ == "__main__":
    sample_data = [
        {"Name": "Alice", "Age": 30, "City": "New York"},
        {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "City": "Chicago"},
    ]

    print(generate_table(sample_data))
