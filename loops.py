"""
loops : for
"""

for i in range(0,10):
    print(i,"^2 :", i**2)

for j in range(0,100,9):
    print(j)


loop = True

while loop:
    name = input("Enter your name: ")
    pwd = input("Enter your password: ")
    if len(pwd) < 4:
        print("pwd len should be 8 chars")
        break
print("done")