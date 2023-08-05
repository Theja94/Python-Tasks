"""Write a Python program that executes an operation on a list and
handles an IndexError exception if the index is out of range.
"""

list_ = ["Car", "Jeep", "Bus"]

try:
    list_[6]
except IndexError:
    print("Index is out of range")


