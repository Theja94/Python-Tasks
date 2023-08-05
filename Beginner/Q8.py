"""Write a Python program to calculate the LCM (Least Common
Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36
"""
num1 = int(input("number1 = "))
num2 = int(input("number2 = "))

# Calculating HCF here
for i in range(1, max(num1, num2)):
    if num1 % i == num2 % i == 0:
        hcf = i

# LCM formula
lcm = (num1*num2)//hcf

print("LCM of", num1, "and", num2, "are:", lcm)