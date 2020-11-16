"""
multiple conditions with or,and,not
"""

n1 = int(input("Enter an integer: "))
n2 = int(input("Enter an integer: "))

if(n1 == n2 and  (n1+n2 == (2*n1) or (2*n2))):
    print("two numbers are equal")
    if(n1 % 2 and n2 % 2 != 0):
        print("two numbers are odd")
    else:
        print("two number are even")


if not n1 == 10 :
    print("number is not 10")

a,b = 5,7

if a == 5:
    if b == 7:
        print("x=5, b=7")
    else:
        print("x=5, b!=7")
else:
    print("x!=5")                