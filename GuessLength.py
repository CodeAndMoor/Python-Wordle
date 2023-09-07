def CheckGuessLength():
    UserGuessing = True
    
    #Guessing Loop
    while UserGuessing == True:
        guess = input("Enter your guess")
        #Determine if word is 5 letters long
        if len(guess) != 5:
            print("That guess is not 5 letters. Try again")
        else:
            UserGuessing = False
    return guess