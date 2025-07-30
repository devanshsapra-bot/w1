# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.writelines(["Line 2\n", "Line 3\n"])

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("Full content:")
    print(content)

with open("example.txt", "r") as f:
    print("Reading line by line:")
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

