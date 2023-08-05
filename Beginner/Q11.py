"""Write a Python program to calculate the sum of digits of a given
number until the sum becomes a single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced to
on single digit.
Final Output: 6

"""

def add_digits(num):
    # number can be represented as 9x or 9x+k 
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    else:
        return num % 9


user_input = int(input("Input: "))
print(f"Final Output: {add_digits(user_input)}")