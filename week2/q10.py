import sys
import textwrap

filename = sys.argv[1]
width = int(sys.argv[2])

with open(filename, 'r') as f:
    for line in f:
        wrapped_lines = textwrap.wrap(line.rstrip('\n'), width)
        for wline in wrapped_lines:
            print(wline)
