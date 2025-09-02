# Practical Example 13: Single inheritance
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

c = Child()
c.greet()

# Practical Example 14: Multilevel
class A: pass
class B(A): pass
class C(B): pass

# Practical Example 15: Multiple
class X: pass
class Y: pass
class Z(X, Y): pass

# Practical Example 16: Hierarchical
class Base: pass
class Child1(Base): pass
class Child2(Base): pass

# Practical Example 17: Hybrid
class P: pass
class Q(P): pass
class R(P): pass
class S(Q, R): pass

# Practical Example 18: super()
class Base:
    def show(self):
        print("Base method")

class Derived(Base):
    def show(self):
        super().show()
        print("Derived method")

d = Derived()
d.show()
