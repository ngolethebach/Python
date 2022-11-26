# Shopping list


print("Welcome To Shopping List!")
myTup = ()
myList = []

for x in range(5):
    itemName = input("Enter item name: ")
    itemPrice = input("Enter item price: ")
    myTup = (itemPrice, itemName)
    myList.append(myTup)

myList.sort(reverse=True)

for x in range(len(myList)): 
    print(myList[x][1] + " = " + myList[x][0])