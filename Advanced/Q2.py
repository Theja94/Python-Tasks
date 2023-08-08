"""Write a program to count the lines in a file “demo.txt”
"""
import os

cwd = os.getcwd()
path_ = os.path.join(cwd,"demo.txt")


with open( path_,'r') as file:
   li = file.readlines()
total_line = len(li)
print(f"Number of lines in the file: {total_line}")
file.close()
