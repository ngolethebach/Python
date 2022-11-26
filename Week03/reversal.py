# Reversing an integer


while True:
    user_input=input("Enter an integer of at least 2 digits and less than 11 digits or -1 to quit: ")
    if user_input == "-1":
        break
    elif len(user_input) <2 or len(user_input) >12:
        print("Your input is invalid, please try again")
    elif int(user_input)<1:
        print("Your input is invalid, please try again")
    else:
        print("Your integer reversed is: {}".format(user_input[::-1]))
print("Program end...")
    





