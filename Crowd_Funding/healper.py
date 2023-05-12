import re
#email validation
def email_validation(Email):
    pattern_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.match(pattern_regex , Email)
# ________________________________
#egyption phone number validation
def phone_validation(phone):
    pattern_regex = r'^01[0125][0-9]{8}$'
    return re.match(pattern_regex , phone)
# ____________register fun________
def register():
    fName = input("Please enter your first name: ")
    lName = input("Please enter your last name: ")
    Email = input("Please enter your email : ")
    while not email_validation(Email):
        Email = input("Invalid email address. Please enter a valid email address: ")
    password = input("Please enter your password: ")
    confirmPassword = input("Please Confirm your password: ")
    while password != confirmPassword:
        confirmPassword = input("Passwords don't match.Please try again: ")
    Phone = input("Please enter your phone number: ")
    while not phone_validation(Phone):
        Phone = input("Invalid phone number. Please enter a valid Egyptian phone number: ")
    with open("users.txt", "a") as file:
        file.write("{} {} {} {} {} \n".format(fName, lName, Email, password, Phone ))
    print("Successful Registeration.")

# __________user login_________
def login():
    Email = input("Please enter your email : ")
    Password = input("Enter your password: ")
    with open("users.txt", "r") as file:
        for line in file:
            user_data = line.strip().split()
            if user_data[2] == Email and user_data[3] == Password:
                print("you Login successfully.")
                print("Welcome, {} {}!".format(user_data[0], user_data[1]))
                return
    print("Invalid email or password. Please try again.")