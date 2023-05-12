from Crud_projects import *
def ProjectMenu():
    print("\n 1- Create Project \n 2- View All Projects \n 3- Edit Project \n 4- Delete Project \n 5- Search For Project \n 6- Exit")

    choice = int(input("\nPlease choose from menu :\n"))
    if choice == 1:
        createProject()

    elif choice == 2:
        # view(user_id)
        displayAllProject()
        # print("2")
        
    elif choice == 3:
        editProject()
        # print("3")

    elif choice == 4:
        deleteProject()

    elif choice == 5:
        # search_by_date()    
        print("5")
    elif choice == 6:
              exit()

    else:
        print("\n Please choose a valid choice")
    

