"""Write a Python program to reverse a number using a while
loop.
Sample Input: num = 12345
Sample Output: revnum = 54321
"""

num = int(input("Input: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))