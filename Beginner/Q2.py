"""
Write a program that accepts a string as input from the user and
calculates the number of digits and letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3
"""
import re


def calc_alpha_num(inp):
    digits = len(re.findall('[0-9]',inp))
    letters = len(re.findall('[A-z]', inp))
    print(f"Output: Alphabets:{letters} & Number: {digits}")


usr_input = input("Give your input \n")
calc_alpha_num(usr_input)