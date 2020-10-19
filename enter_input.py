#input prompt
"""
input has an optional parameter, which is the prompt string.

If the input function is called, the program flow will be stopped until the user has given an input and has ended the input with the return key. The text of the optional parameter, i.e. the prompt, will be printed on the screen.

The input of the user will be returned as a string without any changes. If this raw input has to be transformed into another data type needed by the algorithm, we can use either a casting function or the eval function.
"""

name = input("enter name(max 20 chars)\t")
age = int(input("ente age (1-150)\t"))

print(
    "\nGreetings!, Welcome ", name,
    "\nage ", age)