from APIMethods import DictionaryAPI as DA

def CheckGuessValidity():
    #Bools for both loops
    UserGuessing = True
    
    #Guessing Loop
    while UserGuessing == True:
        guess = input("Enter your guess")
        #Determine if word is 5 letters long
        if len(guess) != 5:
            print("That guess is not 5 letters. Try again")
        #Determine if word is real
        else:
            UserGuessing == False
    
    return guess