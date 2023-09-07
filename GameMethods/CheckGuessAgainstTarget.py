def CheckGuessAgainstTargetWord(guess, TargetWord):
    #Initialize Guess Results for Check Loop
    LetterList     = []
    TargetList     = list(TargetWord)

    #Check Guess Loop
    for i in range(5):
        if guess[i] == TargetWord[i]:
            LetterList.append(guess[i])
            TargetList[i] = "*"
        elif guess[i] in TargetList:
            LetterList.append("*")
            TargetList[TargetList.index(guess[i])] = "*"
        else:
            LetterList.append("_")

    #Concat String
    results = "".join(LetterList)
    
    return results