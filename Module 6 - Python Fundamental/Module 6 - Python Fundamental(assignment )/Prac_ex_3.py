# Practical Example 3: How to take user input using the input() function

n=int(input("enter a number to check prime or not:"))
flag=0
for i in range(2,n):
  if n%i==0:
    flag==1
    break

if flag ==1:
  print("number is not prime")
else:
  print("number is prime")