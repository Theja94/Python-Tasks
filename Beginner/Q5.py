"""
Write a Python program to find the factorial of a number using a
for loop.
"""


def factorial(num):
    fact=1
    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            fact = fact*i
    return fact

inp = input("Input:")
print(f"Factorial: {factorial(int(inp))}")