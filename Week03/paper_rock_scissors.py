# Child's Play


from random import randint


computer_win = 0
user_win = 0
game_play = 0
t= ["rock", "paper", "scissors"]
while computer_win <3 and user_win <3:
    player_choose = str(input("Enter your selection: ")).lower()
    print("You chose: ", player_choose)
    computer_choose = t[randint(0,2)]
    print("The computer chose: ", computer_choose)
    game_play += 1
    if player_choose == computer_choose:
        print("It was a draw")
        print("You need {} to complete this game".format(3-user_win))
        print("Computer need {} to complete this game".format(3-computer_win))
    elif player_choose == "rock":
        if computer_choose == "paper":
            print("The computer won")
            computer_win += 1
            print("You need {} to complete this game".format(3-user_win))
            print("Computer need {} to complete this game".format(3-computer_win))
        elif computer_choose == "scissors":
            print("You win")
            user_win += 1
            print("You need {} to complete this game".format(3-user_win))
            print("Computer need {} to complete this game".format(3-computer_win))
    elif player_choose == "scissors":
        if computer_choose == "rock":
            print("The computer won")
            computer_win += 1
            print("You need {} to complete this game".format(3-user_win))
            print("Computer need {} to complete this game".format(3-computer_win))
        elif computer_choose == "paper":
            print("You win")
            user_win += 1
            print("You need {} to complete this game".format(3-user_win))
            print("Computer need {} to complete this game".format(3-computer_win))
    elif player_choose == "paper":
        if computer_choose == "scissors":
            print("The computer won")
            computer_win += 1
            print("You need {} to complete this game".format(3-user_win))
            print("Computer need {} to complete this game".format(3-computer_win))
        elif computer_choose == "rock":
            print("You win")
            user_win += 1
            print("You need {} to complete this game".format(3-user_win))
            print("Computer need {} to complete this game".format(3-computer_win))
    else:
        print("Check spelling again")
    print("*"*30)
if user_win == 3:
    print("Commiserations the user won...\nYou won...")
else:
    print("Commiserations the computer won...\nGame over...")
            
        



    
