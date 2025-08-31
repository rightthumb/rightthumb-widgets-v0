import os

def process_paths(file_path, spacer='_'):
    """
    Reads a file containing paths, cleans each path, and saves the cleaned paths back to the file.
    
    Args:
    - file_path (str): The path to the file containing the list of paths.
    - spacer (str): The character to replace spaces with (default is '_').
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        cleaned_lines = []
        for line in lines:
            cleaned_line = line.strip().replace(' ', spacer).replace('/- ', '/_')
            cleaned_lines.append(cleaned_line)

        with open(file_path, 'w', encoding='utf-8') as f:
            for cleaned_line in cleaned_lines:
                f.write(cleaned_line + '\n')

        print(f"Successfully cleaned and saved paths in {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Clean paths in a file by replacing spaces.")
    parser.add_argument('file', help="Path to the file containing paths to clean.")
    parser.add_argument('--dash', action='store_true', help="Use dashes instead of underscores.")
    args = parser.parse_args()

    spacer = '-' if args.dash else '_'
    process_paths(args.file, spacer)

if __name__ == "__main__":
    main()
