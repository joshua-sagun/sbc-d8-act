def register():
    while True:
        print("Create Account")
        username = input("Enter username > ")
        lines = [line.strip() for line in open ("username.txt")]
        if username in lines:
            print("Username is not Exist, Try another username!! ")
        else:
            write = open("username.txt", "a")
            print(username, file=write, end="\n") 
            write.close()
            password = input("Enter password > ")
            write = open("password.txt", "a")
            print(password, file=write, end="\n") 
            write.close()
            exit()

def log_or_changepass():
    print("Login")
    username = input("Username > ")
    lines = [line.strip() for line in open ("username.txt")]
    if username in lines:
        user = lines.index(username)
        lines = [line.strip() for line in open ("password.txt")]
        passwordlist = lines[user]
        while True:
            password = input("Password > ")
            if password == passwordlist:
                print("Login sucessfully!")
                print("|Welcome to your account. to change pass pls type 'changepass', to exit type 'ext'|")  
                while True:

                    todo = input("What do you want to do? ")
                    if todo.capitalize() == 'Changepass':
                        lines = [line.strip() for line in open ("password.txt")]
                        oldpassword = input("Enter current password > ")
                        while True:
                            if oldpassword == passwordlist:
                                newpass = input("Enter new password > ")
                                lines[user] = newpass
                                write = open("password.txt", "w")
                                for i in lines:
                                    print(i, file=write, end="\n") 
                                write.close()
                                exit()


                            else:
                                print("That is not you current password !!")
                                exit()
                    elif todo.capitalize() == 'Exit':
                        exit()
                    else:
                        print("What!!")

            else:
                print("Wrong password!! Try again")
    else:
        print("Username do not exist")

while True:
    print("""
Option!;              Keyword!:

Register account    'Register'  
                
Login your account       'login'

Exit                'exit'

""")
    
    user = input("Enter keyword > ")
    if user.lower() == "register":
        register()

    elif user.lower() == "login":
        log_or_changepass()

    elif user.lower() == "exit":
        exit()

    else:
        print("Wrong keyword!!")