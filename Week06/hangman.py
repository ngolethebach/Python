# Hangman


word=list(input("Enter word to be guessed: ").lower())
guessed_word=list(len(word)*"_")
guessed=False
guesses=0
while guessed==False:
    print("Display: "," ".join(guessed_word))
    user_guess=input("Guess a letter: ").lower()
    for i in range(len(word)):
        if user_guess==word[i]:
            guessed_word[i]=user_guess
    guesses+=1
    if guessed_word==list(word) or list(user_guess)==list(word):
        print("Display: ", " ".join(guessed_word))
        print("You have guessed the word correctly! It took you {} guesses".format(guesses))
        guessed=True