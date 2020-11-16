"""
lists,tuples
"""

animals = ["monkeys", "lion", "10", 10.1]

for item in animals:
    if item == "tiger":
        print("tiger in list")
    else:
        print(item)        

animals.append("tiger")
print(animals)

r,g,b = (130,190,35)
print(r,"-",g,"-",b)