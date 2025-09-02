# Overloading (by default arguments)
class Math:
    def add(self, a=0, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(2, 3))
print(m.add(1, 2, 3))

# Overriding
class Parent:
    def display(self):
        print("Parent display")
class Child(Parent):
    def display(self):
        print("Child display")

obj = Child()
obj.display()
