# reverse.py
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = f.readlines()

for line in reversed(lines):
    print(line, end='')
