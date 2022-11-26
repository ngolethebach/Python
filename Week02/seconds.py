# A matter of time


user_second = int(input("Enter second value: "))
minutes,seconds=divmod(user_second,60)
hours,minutes=divmod(minutes,60)
print("%-7s%10s%10s%10s"% ("Input", "Hours", "Minutes", "Seconds"))
print("%-7s%10s%10s%10s"% (user_second,hours,minutes,seconds))