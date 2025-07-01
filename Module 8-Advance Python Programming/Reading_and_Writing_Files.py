# Write a Python program to read the contents of a file and print them on the console

f = open("text.txt","r")
data = f.read()
print(data)
f.close()

#  Write a Python program to write multiple strings into a file.

f= open("text.txt","w")
f.write("\n How are you")
f.write("\n In which Field you are")
f.write("\n Bye")
f.close()

# Write a Python program to check the current position of the file cursor using tell().

with open("text.txt",'r') as f:
    f.seek(15)
    print(f.tell())
    data = f.read()
    print(data)
    print(f.tell())