#!/bin/bash
# Script to parse a CSV file

FILE="data.csv"

while IFS=, read -r column1 column2 column3; do
    echo "Column 1: $column1, Column 2: $column2, Column 3: $column3"
done < "$FILE"
