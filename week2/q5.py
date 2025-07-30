def lensort(strings):
    return sorted(strings, key=len)

def extsort(files):
    return sorted(files, key=lambda f: f.split('.')[-1] if '.' in f else '')

print(lensort(["apple", "fig", "banana", "kiwi"]))


print(extsort(["file.txt", "archive.zip", "image.jpeg", "notes", "script.py"]))

