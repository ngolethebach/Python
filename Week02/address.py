# Address


user_surname = str(input("Enter your surname: "))
house_number = int(input("Enter your home number: "))
road_name = str(input("Enter your road name: "))
town_name = str(input("Enter your town name: "))
                
                
# print("Mr and Mrs ", user_surname, "\n", house_number, ",",road_name, "\n", town_name)
      
      
print("""Mr and Mrs {0},
{1}, {2},
{3}""".format(user_surname, house_number,road_name,town_name ))    