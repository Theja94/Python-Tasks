"""Write a Python program to find if a given string starts with a
given character using Lambda.
Sample input: input_string = "Hello, World!", given_char = "H"
Sample Output: True
"""

inp_string = input("Enter the string: ")
inp_char = input("Enter the char: ")

res = lambda x: True if inp_string.startswith(inp_char.upper()) else False

print(res(inp_string.upper()))