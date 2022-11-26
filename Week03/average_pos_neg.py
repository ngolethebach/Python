# Average of Positive and Negative



def avg_pos_and_neg():
    avg_neg=0
    avg_pos=0
    input_list = []    
    for i in range(10):
        num = int(input("Enter number: "))
        input_list.append(num)
    print("The list: ", input_list)
    count_pos = 0
    count_neg = 0
    sum_pos = 0
    sum_neg = 0
    for j in input_list:
        if j > 0:
            count_pos += 1
            sum_pos += j
            avg_pos = sum_pos/count_pos
        elif j < 0:
            count_neg += 1
            sum_neg += j
            avg_neg = sum_neg/count_neg
        
    print("The sum of pos: ", sum_pos)
    print("The avg of pos: ", avg_pos)
    print("The sum of neg: ", sum_neg)
    print("The avg of neg: ", avg_neg)
    
avg_pos_and_neg()
    
    
