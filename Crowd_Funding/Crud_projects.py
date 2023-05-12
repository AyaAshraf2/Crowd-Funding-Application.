import datetime
import time
import re

def generate_id():
    return round(time.time())

def AskForString(message):
    while True:
        instream = input(message)
        if instream.isalpha():
            return instream
        print("Please try again ")

def AskForInt(message):
    while True:
        int_num = input(message)
        if int_num.isdigit():
            return int_num
        print("Please try again")

def findAllProject(project_id):
    projects = getAllProjects()
    for project in projects:

        print(project)
        project_details = project.strip('\n').split(" ")  
        if project_details[0]==str(project_id):
            return project
    else:
        return False
    # saving projects
def saveProjects(listofprojects):
    try:
        fileobj =open("ProjectData.txt", 'w')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(listofprojects)
        fileobj.close()
        return True

#___ delete projects from file_______
def deleteproject(project):
    projects= getAllProjects()
    projects.remove(project)  
    deleted = saveProjects(projects)
    return deleted

#_______ date validation______
def validateTime(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

def getAllProjects():
    try:
        fileobj =open("ProjectData.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        users = fileobj.readlines()
        return users

# __________create project__________
def createProject():
    Title = input("please enter the title of your project: ")
    Details = input("Please enter the details of your project: ")
    Target = input("Please enter the total target for your project : ")
    Email = input("Please enter your email ")
    while not Target.isdigit():
        Target = input("Invalid target. Please enter a valid amount: ")
    startTime = input("Please enter the start time for your project (YYYY-MM-DD HH:MM:SS): ")
    while not validateTime(startTime):
        start_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
    endTime = input("Please enter the end time for your project (YYYY-MM-DD HH:MM:SS): ")
    while not validateTime(endTime):
        endTime = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
    id = generate_id()
    with open("ProjectData.txt", "a") as file:
        file.write("{} {} {} {} {} {} {}\n".format(id , Title, Details, Target, startTime, endTime, Email ))
    print("Project created successfully.")

# ________view projects_______________
def displayAllProject():
    projects = getAllProjects()
    if projects:
        for project in projects:
            print(project)
    else:
        print(' Error happened please try again ')

#_________edit projects__________ 
def editProject():
    project_id = AskForInt("Please enter the id of the project you want to edit: ") # int
    Email=input("Please enter your email ")
    foundProject = findAllProject(project_id)
    test = str(foundProject).split() 
    if foundProject :
        print( "found" )
        print(test)
        if test[8]== str(Email):
            deleted=deleteproject(foundProject)
            title = input("Please enter the title of your project: ")
            details = input("Please enter the details of your project: ")
            target = input("Please enter the total target for your project (in EGP): ")
            email = input("Please enter your email ")
            while not target.isdigit():
                target = input("Invalid target amount. Please enter a valid amount (in EGP): ")
            start_time = input("Enter the start time for your project (YYYY-MM-DD HH:MM:SS): ")
            while not validateTime(start_time):
                start_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
            end_time = input("Enter the end time for your project (YYYY-MM-DD HH:MM:SS): ")
            while not validateTime(end_time):
                end_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
            id = generate_id()
            with open("ProjectData.txt", "a") as file:
                file.write("{} {} {} {} {} {} {}\n".format(id , title, details, target, start_time, end_time, email ))
            print("Project edited successfully.")
        else:
            print("this project you can't edit it ")


#__________ delete project from file_________
def deleteProject():
    project_id = AskForInt("Please enter the id of the project you want to delete it: ") # int
    Email=input("Please enter your email ")
    foundProject = findAllProject(project_id)
    test = str(foundProject).split() 
    if foundProject :
        print( "found" )
        if test[8]== str(Email):
            deleted=deleteproject(foundProject)
            if deleted:
                print('project deleted successfully')
            else:
                print(" problem happened while deleting the project ")
        else:
            print("this project is not yours to delete ")
            return
    else:
        print("project not found, please try again with valid id ")


    # _____________search______________________
    
# def find_project_by_date(date):
#     projects = getAllProjects()
#     for project in projects:
    
#         project_details = project.strip('\n').split(":")  # list book_details
#         if project_details[4]==str(date) or project_details[5]==str(date):
#             return True , project
#     else:
#       return False
    
# def search_by_date():
#      date=validateTime("Please enter the date to be searched for: ")
#      found=find_project_by_date(date)
#      if found :
#             print("--- project found ")
#             print(found[1])        

#      else:
#         print("project not found, please try again with valid id ")

# def get_all_projects_from_file():
#     try:
#         fileobj =open("projects.txt", 'r')
#     except Exception as e:
#         print(e)
#         return False
#     else:
#         projects = fileobj.readlines()
#         return projects
    

# def askfordate(date):
#     dateregex=re.compile(r'\d{4}[-/]\d{2}[-/]\d{2}')
#     while True:
#         instr=input(date)
#         if re.fullmatch(dateregex,instr):
#             return instr
#         print("----Error --> please enter it again-----")