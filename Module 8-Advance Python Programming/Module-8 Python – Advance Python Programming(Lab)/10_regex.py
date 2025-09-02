import re

# Practical Example 23
text = "Hello, my name is Vishal"
result = re.search("Vishal", text)
if result:
    print("Found:", result.group())

# Practical Example 24
result = re.match("Hello", text)
if result:
    print("Match found:", result.group())
