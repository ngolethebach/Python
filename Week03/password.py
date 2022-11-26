# Check password


pwd = "Rocket"
while True:
    user_pwd = str(input("Enter the password: "))
    if pwd == user_pwd:
        print("Welcome")
        break 
    else:
        print("Try again")