"""You need to write a function that accepts an encoded string as a
parameter.
This string will contain a first name, last name, and an id.
Values in the string can be separated by any number of zeros. The
id is a numeric value but will contain no zeros. The function should
parse the string and return a Python dictionary that contains the
first name, last name, and id values.
For example:
Input : “Robert000Smith000123”
Output:
{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }
"""
import re 

key_list = ["First Name", "Last Name", "id" ]
def decode_str(string_):

    x = re.split('0+', string_)
    res = dict(zip(key_list, x))
    return res


if __name__ == "__main__":
    usr_inpt = "“Robert0Smith000123”"
    print(decode_str(usr_inpt))