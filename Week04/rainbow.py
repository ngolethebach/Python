# Colorful


colorful = ["Red", "Orange", "Yellow", 
            "Green", "Blue", "Indigo", "Violet"]


while True:
    try:
        user_input = int(input("Select number 1 to 7 or press -1 to end program: "))
        if user_input == -1:
            print("Program end")
            break
        elif user_input > 0 and user_input <= len(colorful):
            print(colorful[user_input - 1])
        else:
            print("Invalid number")
    except ValueError:
        print("Try to put integer number")
        