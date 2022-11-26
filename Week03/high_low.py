# Nothing for a Pair


import random 
random_number1 = random.randint(1,13)
if random_number1 == 1:
    print("The value is: Ace")
elif random_number1 in range(2,10):
    print("The value is: ", random_number1)
elif random_number1 == 11:
    print("The value is: Jack")
elif random_number1 == 12:
    print("The value is: Queen")
else:
    print("The value is: King")

random_number2 = random.randint(1,13)
user_guess = str(input("Guess the next card will be higher or lower: "))
print("The second card is: ", random_number2)
if user_guess == "higher" and random_number1 < random_number2:
    print("You win")
elif user_guess == "lower" and random_number1 > random_number2:
    print("You win")
else:
    print("You lose")
