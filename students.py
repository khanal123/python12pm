import os.path
from getpass import getpass

if not os.path.exists('database.txt'):
    fs = open('database.txt', 'w')
    fs.close()


def register():
    userName = input("Enter username:")
    password = getpass("Enter password:")
    print(password)
    if userName in open('database.txt', 'r').read():
        print("Username already exists")
        exit()
    handle = open('database.txt', 'a')
    handle.write(userName)
    handle.write(" ")
    handle.write(password)
    handle.write("\n")
    handle.close()
    print("User was successfully created")


def login():
    userName = input("Enter username:")
    password = getpass("Enter password:")
    get_data = open('database.txt', 'r').readlines()
    get_users = []
    for data in get_data:
        get_users.append(data.split())
    total_users = len(get_users)
    increment = 0
    login_success = False
    while increment < total_users:
        uname = get_users[increment][0]
        upass = get_users[increment][1]
        if userName == uname and password == upass:
            login_success = True
        increment += 1
    if login_success == True:
        print(f"Welcome {userName}")
    else:
        print("Username & password don't match")


question = input("Do you have an account?")
print("Enter y or Y if yes and n or N if no")
if question == 'y' or question == 'Y':
    login()
else:
    register()
