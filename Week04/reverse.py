# Reversal


input_list = []


for i in range(5):
    input_list.append(int(input("Enter number: ")))
for j in range(5,0,-1):
    print(input_list[j-1])
    