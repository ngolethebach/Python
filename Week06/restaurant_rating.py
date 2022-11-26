# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:06:43 2021

@author: The Bach
"""

# Rate a restaurant



user_choice = 0
def log_error(user_choice):
    user_rate = 0
    user_total = 0
    while True:
        try:
            user_choice = int(input("Rate a restaurant 1-5: "))
            if not (0 < user_choice < 6) and user_choice != -1:
                raise Exception("Number out of range: " + str(user_choice))
            if user_choice == -1:
                break
        except ValueError as err:
            print("Entry must be int ")
            log_error(err)
        except Exception as err:
            print("Number must be from 1-5")
            log_error(err)

        user_rate += 1
        user_total += user_choice
        avg = user_total / user_rate

    print("There are {} people rating".format(user_rate))
    print("Avg rating: {}".format(avg))
    
        
log_error(user_choice)
      
    

    