"""#1.
a = 3
b = 4
print(f"before swapping:{a,b}")

a, b= b, a
print(f"After swapping:{a,b}")
"""""
#2.
"""
import math

x1= float( input("enter x1:"))
y1= float( input("enter y1:"))
x2= float( input("enter x2:"))
y2= float( input("enter y2:"))
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)
"""
#3.
"""
num = int(input("Enter a number: "))

if num % 2 == 0:
   print("The number is even")
else:
   print("The number is odd")
"""
#4

"""
v = ["a", "e", "i", "o", "u"]

c = input("Enter a character: ")

if c.lower() in v:
    print("Vowel")
else:
    print("Not a vowel")
"""

#5
"""
marks= float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
   print("Grade: A+")
elif marks >= 85:
    print("Grade: A")
elif marks >= 80:
   print("Grade: B+")
elif marks >= 75:
  print("Grade: B")
elif marks >= 70:
  print("Grade: C+")
elif marks >= 65:
  print("Grade: C")
elif marks >= 60:
    print("Grade: D+")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")
"""
