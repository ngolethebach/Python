# Shopping List



print("Peaches")
peach_number = int(input("-how many? "))
peach_price = float(input("-price? "))

print("Beans")
bean_number = int(input("-how many? "))
bean_price = float(input("-price? "))

print("Chicken pieces")
chicken_piece_number  = int(input("-how many? "))
chicken_piece_price = float(input("-price? "))

print("Socks")
sock_number = int(input("-how many? "))
sock_price = float(input("-price? "))

print("Bottle of water")
bottle_number = int(input("-how many? "))
bottle_price = float(input("-price? "))

total_number_item = peach_number + bean_number + chicken_piece_number + sock_number + bottle_number
total_cost = peach_price * peach_number + bean_number * bean_price + chicken_piece_number * chicken_piece_price + sock_number * sock_price + bottle_number * bottle_price 

print("Total number of items purchased: ", total_number_item)
print("Your weekly shop cost: ", total_cost)
