# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 21:34:47 2021

@author: The Bach
"""

# Secure entry


print("1. New user\n2. Existing user", end = "\n")
user_option = input()
if user_option == "1":
    new_user_name = input("Enter a username: ")
def password_check(new_user_pass):
    user = True
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while user:
        if (len(new_user_pass) < 8):
            print("Password must be at least 8 characters long")
            user = False
        if (" " in new_user_pass):
            print("Password cant begin, end or contain a space")
            user = False
        if new_user_pass[0] in nums: 
            print("Password cant begin with number")
            user = False
        if user:
            return user
    
def main():
    new_user_pass = input("Enter a password: ")
    if (password_check(new_user_pass)):
        print("Password is valid")
    else:
        print("Invalid password")
if __name__ == '__main__':
    main()
        



                              