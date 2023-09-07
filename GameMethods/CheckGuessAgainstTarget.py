def CheckGuessAgainstTargetWord(guess, TargetWord):
    #Initialize Guess Results for Check Loop
    LetterList = []

    #Check Guess Loop
    for i in range(5):
        if guess[i] == TargetWord[i]:
            LetterList.append(guess[i])
        elif guess[i] in TargetWord:
            LetterList.append("*")
        else:
            LetterList.append("_")

    #Concat String
    results = "".join(LetterList)
    
    return results