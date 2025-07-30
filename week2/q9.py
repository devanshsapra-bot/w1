import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    for line in f:
        print(line.rstrip('\n')[::-1])
