import sys
def convert_to_markdown_table(records, columns='', abbreviations=False):
    import re

    def abbreviate_column(col):
        # Function to generate abbreviations
        words = re.split(r'[_\-\s]+', col)  # Split by underscore, dash, or space
        abbreviation = ''.join(word[0] for word in words).lower()
        return abbreviation

    def generate_abbreviation_dict(full_columns):
        # Generate a dictionary of abbreviations to column names
        abbr_dict = {}
        for col in full_columns:
            abbr_dict[abbreviate_column(col)] = col
        return abbr_dict

    # Determine the columns to use
    if columns:
        selected_columns = [col.strip() for col in columns.split(',')]
    else:
        selected_columns = list(set(key for record in records for key in record.keys()))

    # Generate abbreviations dictionary
    abbrev_dict = generate_abbreviation_dict(selected_columns)

    # Prepare the header of the markdown table
    if abbreviations:
        header = [abbreviate_column(col) for col in selected_columns]
        abbrev_yaml = '\n'.join(f"{k}: {v}" for k, v in abbrev_dict.items())
        print(abbrev_yaml)  # Print abbreviations as YAML
        sys.exit()
    else:
        header = selected_columns
    
    # Create the markdown table string
    markdown_table = '| ' + ' | '.join(header) + ' |\n'
    markdown_table += '| ' + ' | '.join(['---']*len(header)) + ' |\n'
    
    for record in records:
        row = [str(record.get(col, '')) for col in (abbrev_dict.values() if abbreviations else selected_columns)]
        markdown_table += '| ' + ' | '.join(row) + ' |\n'

    return markdown_table

# Example usage:
records = [
    {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'},
    {'Name': 'Bob', 'Age': 25, 'Occupation': 'Designer'}
]

# Convert to markdown with specifications
markdown_table = convert_to_markdown_table(records, columns='Name, Age', abbreviations=False)
# markdown_table = convert_to_markdown_table(records, columns='', abbreviations=False)
# markdown_table = convert_to_markdown_table(records, columns='Name, Age', abbreviations=True)
print(markdown_table)
