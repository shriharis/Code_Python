"""
if elif and else usage
"""
age = int(input("Enter your age[1-100]: "))

if age < 1:
    print("invalid argument:input value between 1-100")
elif age < 16:
    print("You are NOT eligible for Driving Licence")
elif age >= 16:
    print("You are eligible for Driving Licence")