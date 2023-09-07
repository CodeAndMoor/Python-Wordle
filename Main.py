from GetWord import GetWord

#Get word for this play
TargetWord = GetWord()

#Handle API Errors
if TargetWord == "Error":
    print("The API seems to be down. Please try again later")

UserGuessing = True

#Guessing Loop
while UserGuessing == True:
    guess = input("Enter your guess")
    
    #Determine if word is 5 letters long
    if len(guess) != 5:
        print("That guess is not 5 letters. Try again")
    else:
        UserGuessing = False

#Initialize Guess Results for Check Loop
GuessResults = ""

#Check Letters Loop
for i in range(5):
    if guess[i] == TargetWord[i]:
