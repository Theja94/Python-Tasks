"""
Write a Python program to input marks for five subjects Physics,
Chemistry, Biology, Mathematics, and Computer. Calculate the
percentage and grade according to the following:

Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F

"""

print(" Max marks : 100 \n")
physics=int(input("Input marks of Physics: "))
chemistry=int(input("Input marks of Chemistry: "))
biology=int(input("Input marks of Biology: "))
maths=int(input("Input marks of Mathematics: "))
computer=int(input("Input marks of Computer: "))
sum=(physics+chemistry+biology+maths+computer)
percent = int((sum/500)*100)

if(percent>=90):
    print("Grade: A")
elif(percent>=80 & percent<90):
    print("Grade: B")
elif(percent>=70 & percent<80):
    print("Grade: C")
elif(percent>=60 & percent<70):
    print("Grade: D")
elif(percent>=40 & percent<60):
    print("Grade: E")
else:
    print("Grade: F")