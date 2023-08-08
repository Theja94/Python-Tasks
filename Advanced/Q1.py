"""Read the doc.txt file using Python File handling concept and
return only the even length string from the file. Consider the
content of doc.txt as given below:
Hello I am a file
Where you need to return the data string which is of even length.
Make sure you return the content in The same link as it is present."""

import os

cwd = os.getcwd()
path_ = os.path.join(cwd,"demo.txt")
list_ = []
with open( path_,'r') as file:
    li = file.read()
    s = li.split(" ")
    for i in s:
        if len(i)%2 == 0:
            list_.append(i)
    print(*list_, sep = ", ")
    file.close()