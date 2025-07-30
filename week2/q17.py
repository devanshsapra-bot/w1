from collections import defaultdict

def find_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = ''.join(sorted(w))
        groups[key].append(w)
    
    return [group for group in groups.values() if len(group) > 1]
