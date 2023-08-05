"""Write a Python program to find the common elements between
two lists.
"""

def common_element(a, b):
	res = [i for i in a if i in b]
	return res


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 6, 7, 8, ]

    print("The common elements in the two lists are: " + str(common_element(a, b)) )
