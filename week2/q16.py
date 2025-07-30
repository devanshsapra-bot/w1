from collections import Counter
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    text = f.read()

freq = Counter(text)
for char, count in freq.most_common():
    print(f"'{char}': {count}")
