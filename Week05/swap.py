# Swap


def swap_positions():
    input_list = []
    for i in range(2):  
        num = int(input("Enter two number: "))
        input_list.append(num)
    print("The list: ", input_list)
    reversed_list = []
    for j in range(2, 0, -1):
        reversed_list.append(input_list[j-1])
    print("Reverse list: ", reversed_list)
    

swap_positions()