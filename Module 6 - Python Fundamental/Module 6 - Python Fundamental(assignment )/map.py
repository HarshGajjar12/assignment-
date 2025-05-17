# Write a Python program to apply the map() function to square a list of numbers.
def square(a):
  return a*a

l=[10,20,30,40,50]
a=list(map(square,l))
print(a)
  