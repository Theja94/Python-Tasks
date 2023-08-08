"""Write a program to construct a dictionary from the two lists
containing the names of students and their corresponding
subjects. The dictionary should map the students with their
respective subjects. Let’s see how to do this using for loops and
dictionary comprehension.
Input: [Sam, Alice, Mona] ,

[Commerce, Science, Computer]

Output: [Sam: Commerce, Alice: Science , Mona: Computer]
"""

_keys = ["Sam", "Alice", "Mona"]
_values = ["Commerce", "Science", "Computer"]


# using for loops
# res = {}
# for key in _keys:
#     for value in _values:
#         res[key] = value
#         _values.remove(value)
#         break


# using dictionary comprehension
res = {_keys[i]: _values[i] for i in range(len(_keys))}

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))
