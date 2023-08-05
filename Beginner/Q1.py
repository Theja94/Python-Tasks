
def division(number):
    if number % 3 == 0 and number % 5 == 0:
        print("ConsultAdd-Python Training")
    elif number % 5 == 0:
        print("Python Training")
    elif number % 3 == 0:
        print("ConsultAdd")
    else:
        print("Number is invalid")


userinput = input("Enter an integer \n")
division(int(userinput))

