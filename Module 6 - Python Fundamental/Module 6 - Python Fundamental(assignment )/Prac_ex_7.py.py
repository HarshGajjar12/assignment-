# Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder
marks=int(input("enter your marks:"))

if marks >90:
  print("Grade A")
elif marks >70 and marks<=90:
  print("Grade B")
elif marks >50 and marks<=70:
  print("Grade C")
elif marks >35 and marks<=50:
  print("Grade D")
else:
  print("Fail")