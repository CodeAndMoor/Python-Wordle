from APIMethods.DictionaryAPI import CheckWord as CW

def CheckGuessValidity():
    #Bools for both loops
    UserGuessing = True
    
    #Guessing Loop
    while UserGuessing == True:
        #Initialize Variables
        WordIsRealString = ""
        
        #User Input
        guess = input("Enter your guess: ")
        
        #Determine if word is 5 letters long
        if len(guess) != 5:
            print("That guess is not 5 letters. Try again")
        #Determine if word is real
        else:
            WordIsRealString = CW(guess)
            #Guess is not a real word
            if WordIsRealString == "False":
                print("That is not a valid guess. Please try again")
            #Api is down
            elif WordIsRealString == "Errors":
                print("The Service Appears to be Down. Please Try again Later")
                guess = "Errors"
                break
            #Guess is a real word
            else:
                UserGuessing = False
    
    return guess