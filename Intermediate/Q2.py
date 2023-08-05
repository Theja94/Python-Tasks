"""Create a function that takes a list and returns a new list with
unique elements of the first list.
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
Sample Output: list2 = [1, 2, 3, 4, 5]
"""

def unique(list1):

	# inserting list to a set
	list_set = set(list1)
	# convert the set to the list
	unique_list = (list(list_set))
	return unique_list


if __name__ == "__main__":
    list_ = [10, 20, 10, 30, 40, 40]
    print("the unique values from list is "+ str(unique(list_)))


