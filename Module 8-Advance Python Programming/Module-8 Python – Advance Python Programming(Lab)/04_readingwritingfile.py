# Practical Example 4: Write string
with open("test.txt", "w") as f:
    f.write("Hello, this is a test string.\n")

# Practical Example 5: Read file
with open("test.txt", "r") as f:
    print("File content:\n", f.read())

# Practical Example 6: File cursor position
with open("test.txt", "r") as f:
    print("Cursor position:", f.tell())
    f.read(5)
    print("Cursor after reading 5 chars:", f.tell())
