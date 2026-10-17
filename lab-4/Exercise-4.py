#1
"""
game = ["resident evil 7", "onimusha", "resident evil village"]
print (game)
for i in range(1, 5):
    print(i)
"""
#2
"""
x= int (input("enter:") )
while x>=0:
    print(x)
    x = x-1
"""
#3
"""
base= 2
power = 2
result = 1
for i in range(power):
    result= result*base
    print (result)
    """
#4
"""
t= 0
for num in range(1, 1000):
    if num % 1==0 and num %num==0:
        t = t +num
        break
print(t)
"""
#5
"""
def fibo(n):
   if n<= 1:
      return n
   return fibo(n-1)+fibo(n-2)

N = int (input("Enter:"))
for i in range(N):
    print (fibo(i))
""" 

