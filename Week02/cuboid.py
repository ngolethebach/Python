# Cuboid


width = int(input("Enter width: "))
length = int(input("Enter length: "))
height = int(input("Enter height: "))


surface_area = 2*(width*length + width*height + length*height)
volume = width * length * height


print("Surface area: ", surface_area)
print("Volume: ", volume)