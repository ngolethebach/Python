# Match the dice


import random 


number_roll = 0
while True:
    number_roll += 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    
    print("First dice: ", dice1)
    print("Second dice: ", dice2)
    
    
    if dice1 == dice2:
        print("\nIt takes {} to match".format(number_roll))
        break
    else:
        print("\nRoll again ")
    

