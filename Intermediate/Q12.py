"""Create a login page backend to ask users to enter the username
and password. Make sure to ask for a Re-Type Password and if the
password is incorrect give a chance to enter it again but it should
not be more than 3 times.
"""
count=0
user_name = input("Enter your Username: ")
password = input("Enter your password: ")
retype_pass  = input("Retype your password: ")

while count<= 3: 
    
    if count > 3:
        print("Unsuccessful")
    if password != retype_pass:
        retype_pass = input("Password does not match, Try again: ")
        count += 1
        
    else:    
        print("User created")
        break
