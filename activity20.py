from getpass import getpass

isLogin = False

While isLogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "admin" and password == "password123":
        print("Login successful!")
        isLogin = True
    else:
        print("Invalid username or password. Please try again.")
        isLogin = False