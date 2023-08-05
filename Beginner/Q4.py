"""
Write a Python program to find the sum of all odd numbers
between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25
"""

def sum_odd(start, stop):
    odd_numbers = []
    for item in range(int(start)+1,int(stop)):
        if item % 2 != 0:
            odd_numbers.append(item)
    return sum(odd_numbers)    


print("Give the two numbers: \n")
num1 = input("Start=")
num2 = input("Stop=")
print(f"Sum of odd numbers: {sum_odd((num1),(num2))} ")