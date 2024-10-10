#!/bin/bash

# Prompt the user to enter the file suffix
read -p "Enter the file suffix (e.g., .sh, .py): " SUFFIX

DIRECTORY=$(pwd)  # Get the current working directory

# Find and submit files ending with the specific suffix
for file in "$DIRECTORY"/*"$SUFFIX"; do
    if [ -f "$file" ]; then
        echo "Submitting $file to SLURM"
        sbatch "$file"
    else
        echo "No files with suffix $SUFFIX found in $DIRECTORY."
        break
    fi
done
