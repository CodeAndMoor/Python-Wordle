from APIMethods.GetWordAPI               import GetWord                     as GW
from GameMethods.GuessValidity           import CheckGuessValidity          as CGV
from GameMethods.CheckGuessAgainstTarget import CheckGuessAgainstTargetWord as CGAT

WantsToPlay = True

while WantsToPlay == True:
    #Get word for this play
    #TargetWord = GW()

    #Debug Line
    TargetWord = "Shots"

    #Handle API Errors
    if TargetWord == "Errors":
            print("The API seems to be down. Please try again later")

    #Set Number of Guesses to 0
    UserAttempts = 0

    #Main Loop while playing the game
    while UserAttempts <= 6:
        guess = CGV()

        #Stops Game if one of the API's is down
        if guess == "Errors":
             break             

        #Win Condition
        if guess == TargetWord:
            print(guess)
            print("You win!") 
        #Check Guess Letters
        else:
            results = CGAT(guess, TargetWord)
            print(results)
            UserAttempts = UserAttempts + 1

    if UserAttempts > 6:
        print("Sorry you lost. The word was " + TargetWord + ".")

    PlayAgainString = input("Would you like to play again? ('y' for yes)")
    if PlayAgainString.lower == "y":
        WantsToPlay = True
    else:
        WantsToPlay = False
        print("Thanks for playing!")