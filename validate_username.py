"""
validaing username
"""

from modules import try_xcept

username = input("Enter username:(only English alphabets allowed) \n")
print(try_xcept.validate(username))

