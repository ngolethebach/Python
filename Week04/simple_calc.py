# A simple calculator


first_number = int(input("Enter a positive integer: "))
second_number = int(input("Enter a positive integer: "))
user_operator = str(input("Choose an operator: "))


if user_operator == "+":
    total = first_number + second_number
    print("Your sum is {} + {} and the answer is {}".format(first_number,second_number,total))
elif user_operator == "-":
    difference = first_number - second_number
    print("Your sum is {} - {} and the answer is {}".format(first_number,second_number,difference))
elif user_operator == "/":
    if second_number == 0:
        print("Invalid value")
    else:
        division = first_number / second_number
        print("Your sum is {} / {} and the answer is {}".format(first_number,second_number,division))
elif user_operator == "*":
    multiplication = first_number * second_number
    print("Your sum is {} * {} and the answer is {}".format(first_number,second_number,multiplication))
else:
    print("Invalid operator")