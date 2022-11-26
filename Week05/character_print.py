# Character Print


def character_print():
    if len(character) == 0 and num == 0:
        return
    character_times = num * character
    print(character_times)
    
    
num = int(input("Enter number: "))
character = str(input("Enter character: "))
character_print()