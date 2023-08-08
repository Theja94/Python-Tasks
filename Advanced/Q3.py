"""Aditi has used text editing software to type some text. After
saving the article as words.txt, she realized that she had wrongly
typed the alphabet “J" instead of “I" everywhere in the article.
Write a function definition for JtoI() in Python that would display
the corrected version of the entire content of the file WORDS.TXT
with all the alphabet "J" to be displayed as an alphabet "I" on the
screen.
Note: Assume that words.txt does not contain any J alphabet
otherwise.
"""

import os

cwd = os.getcwd()
path_ = os.path.join(cwd,"demo.txt")

def jtoi(path_):
    file = open(path_,"r")
    data = file.read()
    for letter in data:
        if letter == 'J':
            print("I",end="")
        else:
            print(letter,end="")

    file.close()

jtoi(path_)