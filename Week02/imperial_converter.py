# Height converter



user_height_feet = int(input("Height in feet: "))
user_heigt_inch = int(input("Height in inch: "))
user_height_km = (user_height_feet * 12 + user_heigt_inch) * 2.54 /100000
user_height_m = user_height_km * 1000
user_height_cm = user_height_m * 100
user_height_mm = user_height_cm * 10


print("Height in kilometres: ", user_height_km)
print("Height in metres: ", user_height_m)
print("Height in centimetres: ", user_height_cm)
print("Height in millimetres: ", user_height_mm)