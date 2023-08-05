"""Write a Python program to count the frequency of each element
in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
"""


def CountFrequency(my_list):

	# Creating an empty dictionary
	freq = {}
	for items in my_list:
		freq[items] = my_list.count(items)
	print(freq)


# Driver function
if __name__ == "__main__":
	my_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
	CountFrequency(my_list)
