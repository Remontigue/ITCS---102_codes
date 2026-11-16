from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "general" and password == "123":
        print("Login successful!")
        isLogin = True
    else:
        print("Wrong username and password. Please dont try anymore.")
        isLogin = False
