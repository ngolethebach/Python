# Cans of paint


import math 


area_of_hall = 3.4*2*(40+30)
number_of_can = area_of_hall/5.1
print("Number of cans required: ", math.ceil(number_of_can))

print("Number of can in box: 8")


volume_of_a_can = math.pi * (0.15/2)**2 * 0.3
volume_of_a_box = 0.6 * 0.3 * 0.35
number_of_full_box = volume_of_a_box/volume_of_a_can
print("Number of full box: ",math.floor(number_of_full_box))


can_not_in_box = number_of_can - math.floor(number_of_full_box)*8
print("Cans not packed in boxes: ", math.ceil(can_not_in_box))


