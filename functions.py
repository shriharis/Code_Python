"""
function to return nth fibonacci number
"""

def fibonacci(n):
    if n <0:
        print("invalid")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
n = int(input("enter n: \n"))
print(fibonacci(n))

