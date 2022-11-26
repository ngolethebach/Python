# Functional Calculator


# Function add 2 numbers
def add(num1, num2):
    return num1 + num2

# Function subtract 2 numbers
def subtract(num1, num2):
    return num1 - num2

# Function multiply 2 numbers
def multiply(num1, num2):
    return num1 * num2

# Function divide 2 numbers
def divide(num1, num2):
    return num1 / num2

# Function remainder 
def remainder(num1, num2):
    return num1 % num2

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ("1", "2", "3", "4", "5"):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if choice == "1":
                print("{} + {} = {}" .format(num1, num2, add(num1, num2)))
            elif choice == "2":
                print("{} - {} = {}" .format(num1, num2, subtract(num1, num2)))
            elif choice == "3":
                print("{} * {} = {}" .format(num1, num2, multiply(num1, num2)))
            elif choice == "4":
                try:
                    print("{} / {} = {}" .format(num1, num2, divide(num1, num2)))
                except ZeroDivisionError:
                    print("Num2 cant be zero")
            elif choice == "5":
                print("{} % {} = {}" .format(num1, num2, remainder(num1, num2)))
            else:
                print("Invalid value")
        except ValueError:
            print("String/float are not allowed")
    elif choice == "-1":
        print("Program ending......")
        break
    else:
        print("Invalid value")            
