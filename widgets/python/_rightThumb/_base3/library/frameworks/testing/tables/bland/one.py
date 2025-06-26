from tabulate import tabulate

data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"},
]

print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
