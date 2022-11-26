# Diamond


width = int(input("Enter the width: "))
if 2 < width < 40:
    for i in range(width):
        print(" " * (width - i) + " *" * (i + 1))
    for j in range(width - 1):
        print(" " * (j + 2) + " *" * (width - j - 1))
else:
    print("Invalid value")