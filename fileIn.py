"""
file IO
"""

file = open('.\data\input.txt','r')
f = file.readlines()

l1 = []
for line in f:
    if line[-1] == '\n':
        l1.append(line[:-1])
    else:
        l1.append(line)
                
print(f)
print(l1)

l2 = []
for line in f:
    l2.append(line.strip())

file.close()
print(l2)
