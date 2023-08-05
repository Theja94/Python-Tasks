"""Write a Python program to check if a string is an anagram of
another string.
string1 = "listen", string2 = "silent"
Output: True
"""


def anagram(s1, s2):
     
    if(sorted(s1)== sorted(s2)):
        print("Output: True")
    else:
        print("Output: False")        
         
s1 =input("string1: ")
s2 =input("string2: ")
anagram(s1, s2)