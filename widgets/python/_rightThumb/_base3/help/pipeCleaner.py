__.setting('pipe-cleaner', {
    # Core behavior
    'first': True,            # Clean first character if unsafe
    'trim': True,             # Strip leading/trailing spaces
    'deep': True,             # Strip tabs/newlines/carriage returns
    'multi': 3,               # Repeat deep cleaning (number of times)

    # Targeted behavior
    'skip': [],               # List of indices to skip cleaning
    'preserve-original': True,   # Save a copy of original pipe in `pipe-original`
    'ignore-if-startswith': ['#', '//'],  # Skip cleaning if line starts with any of these
    'only-clean-if-contains': None,       # Only clean lines that contain this string or list

    # Regex options
    'regex-replace': [        # Apply regex-based replacements
        { 'pattern': r'\s{2,}', 'replace': ' ' },        # collapse multiple spaces
        { 'pattern': r'^\s*#.*$', 'replace': '' }        # remove full-line comments
    ],

    # Custom trimming
    'strip-left': True,       # Strip only left side (overrides 'trim' if specified)
    'strip-right': False,     # Strip only right side

    # Case handling
    'lowercase': False,       # Convert cleaned pipe to lowercase
    'uppercase': False,       # Convert cleaned pipe to uppercase
    'capitalize': False,      # Capitalize each cleaned line

    # Content validation
    'validate-length': {      # Remove or log lines that are too short/long
        'min': 3,
        'max': 200
    },

    # Logging
    'log-cleaning': True,     # Log changes made to pipe data
    'log-skip-reasons': True, # Explain why a line was skipped

    # Compatibility / Extensions
    'safe-prefix': '>',       # If line is unsafe, prefix with this instead of trimming
    'clean-empty': True,      # Remove empty strings from pipe after cleaning
})
