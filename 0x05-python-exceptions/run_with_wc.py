import sys
import subprocess

def wc(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    lines = text.count('\n') + 1
    words = len(text.split())
    chars = len(text)
    print(f"File: {file_name} - Lines: {lines}, Words: {words}, Characters: {chars}")

# Get the script file name from the command line
if len(sys.argv) < 2:
    print("Usage: python run_with_wc.py <script.py>")
    sys.exit(1)

script_file = sys.argv[1]

# Perform the word count check
wc(script_file)

# Run the actual script after wc check
subprocess.run(["python", script_file])

