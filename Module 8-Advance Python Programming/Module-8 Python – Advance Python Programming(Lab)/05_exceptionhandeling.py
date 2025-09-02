# Practical Example 7: Calculator with exception
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input.")

# Practical Example 8: Multiple exceptions
try:
    f = open("no_file.txt", "r")
    print(10 / 0)
except FileNotFoundError:
    print("File not found.")
except ZeroDivisionError:
    print("Division by zero.")
finally:
    print("Finally block executed.")

# Practical Example 10: Custom exception
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
except NegativeNumberError as e:
    print(e)
