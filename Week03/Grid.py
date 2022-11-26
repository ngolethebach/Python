# Grid


column_number = int(input("Number of columns: "))
row_number = int(input("Number of rows: "))
for i in range(column_number):
    for j in range(row_number):
        print("*", end = '')
    print()