def file_stats(filename):
    num_chars = 0
    num_words = 0
    num_lines = 0
    
    with open(filename, 'r') as f:
        for line in f:
            num_lines += 1
            num_chars += len(line)
            num_words += len(line.split())
    
    return num_chars, num_words, num_lines
chars, words, lines = file_stats('example.txt')
print(f"Characters: {chars}, Words: {words}, Lines: {lines}")
