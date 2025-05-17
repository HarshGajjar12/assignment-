# Write a Python program that uses reduce() to find the product of a list of numbers.
from functools import reduce
def mu(l,res):
  return res*l
l=[1,2,3,4,5]
res=1
t=reduce(mu,l)
print(t)