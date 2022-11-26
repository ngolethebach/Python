# Sum of Positive and Negative Integers


input_list = []
for i in range(10):
    input_list.append(int(input("Enter number: ")))
print("Number in list: ", input_list)
sum_of_neg = 0
sum_of_pos = 0
for j in input_list:
    if j < 0:
        sum_of_neg += j
    elif j >0:
        sum_of_pos += j
    else:
        print("Try again")
print("Sum of negative number: {}".format(sum_of_neg))
print("Sum of positive number: {}".format(sum_of_pos))
