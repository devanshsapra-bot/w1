def parse_csv(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            # Remove trailing newline and split on commas
            row = line.rstrip('\n').split(',')
            result.append(row)
    return result
import string

def mutate(word):
    letters = string.ascii_lowercase
    mutations = set()
    length = len(word)
    
    # Insert
    for i in range(length + 1):
        for c in letters:
            mutations.add(word[:i] + c + word[i:])
            
    # Delete
    for i in range(length):
        mutations.add(word[:i] + word[i+1:])
    
    # Replace
    for i in range(length):
        for c in letters:
            if word[i] != c:
                mutations.add(word[:i] + c + word[i+1:])
    
    # Swap
    for i in range(length - 1):
        if word[i] != word[i+1]:
            mutations.add(word[:i] + word[i+1] + word[i] + word[i+2:])
    
    return mutations
