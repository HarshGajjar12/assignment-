# Practical Example 11
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Vishal", 22)
print(s1.name, s1.age)

# Practical Example 12: Local vs Global
x = 10
class Test:
    def show(self):
        x = 20
        print("Local:", x)
        print("Global:", globals()['x'])

t = Test()
t.show()
