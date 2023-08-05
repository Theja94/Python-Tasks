
string = input("Input Sentence: ")
list_ = []
# Splitting by whitespace and reversing
s = string.split()[::-1]

for i in s:
	list_.append(i)

print("Output after reverse: " + " ".join(list_) )	
