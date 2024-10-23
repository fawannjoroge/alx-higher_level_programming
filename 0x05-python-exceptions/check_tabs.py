import sys
import re

def check_tabs(file_name):
    with open(file_name, 'r') as f:
        for i, line in enumerate(f, 1):
            # Check if the line starts with spaces (leading whitespaces)
            if re.match(r'^[ ]+', line):
                print(f"Error: Spaces found on line {i} in {file_name}")
                return False
    return True

# Run the check on all files passed as arguments
for file in sys.argv[1:]:
    if file.endswith('.py'):
        if not check_tabs(file):
            sys.exit(1)  # Exit with an error code if spaces are found

