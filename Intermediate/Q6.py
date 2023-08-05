"""Write a Python program to check if a number is a power of two
using recursion.
"""

def check_power(n):
    n = n//2
    if n == 2:
        return True
    elif n > 2:
        return check_power(n)
    else:
        return False

    
if __name__ == "__main__":

    inp = int(input("Enter the number: "))
    if check_power(inp):
        print(f"The number {inp} is a power of 2")
    else:
        print(f"The number {inp} is not a power of 2")
