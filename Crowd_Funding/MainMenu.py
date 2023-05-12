from healper import register,login
from Crud_projects import *
from Project_Menu import ProjectMenu

def MainMenu():
 while True:
    print("\n CROWD FUNDING CONSOL APP:")
    print("\n Please select your choice:")
    print("1- Register")
    print("2- Login")
    print("3- Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        register()
        # print("your choice 1")
    elif choice == 2:
        # print("your choice 2")
        login()
        while True:
            ProjectMenu()
        else:
            print("try again")
    elif choice == 3:
        # print("your choice 3")
        exit()
    else:
        print("Please enter a valid choice")

MainMenu()