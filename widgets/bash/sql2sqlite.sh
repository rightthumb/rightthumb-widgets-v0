#!/bin/bash

# Function to display help message
show_help() {
  echo "Usage: $0 -d <database_file> -s <sql_dump_file>"
  echo "  -d    Path to the SQLite database file to create or update."
  echo "  -s    Path to the SQL dump file containing the SQL statements."
  echo "  -h    Display this help message."
}

# Parse arguments
while getopts "d:s:h" opt; do
  case $opt in
    d) DATABASE_NAME="$OPTARG" ;;
    s) SQL_DUMP_FILE="$OPTARG" ;;
    h) show_help; exit 0 ;;
    *) show_help; exit 1 ;;
  esac
done

# Check if both arguments are provided
if [[ -z "$DATABASE_NAME" || -z "$SQL_DUMP_FILE" ]]; then
  echo "Error: Both database file and SQL dump file must be provided."
  show_help
  exit 1
fi

# Step 1: Create the SQLite database (if it doesn't already exist)
echo "Creating SQLite database: $DATABASE_NAME"
sqlite3 "$DATABASE_NAME" "VACUUM;"

# Step 2: Populate the SQLite database using the SQL dump
echo "Populating database with SQL dump: $SQL_DUMP_FILE"
sqlite3 "$DATABASE_NAME" < "$SQL_DUMP_FILE"

if [[ $? -ne 0 ]]; then
  echo "Error: Failed to populate the database. Please check the SQL dump file and database path."
  exit 1
fi

# Step 3: List tables in the database
echo "List of tables in the database:"
sqlite3 "$DATABASE_NAME" ".tables"

echo "Database population completed successfully."
