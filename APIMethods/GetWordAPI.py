import requests                      as r
import json                          as j
from APIMethods.DictionaryAPI import CheckWord as DA

#Gets a random, five letter word from an API
def GetWord():
    #Bool for loop
    WordFound = False

    while WordFound == False:
        #URL for the API response
        url = "https://random-word-api.herokuapp.com/word?length=5"
        
        #Results of the API response
        response = r.get(url)

        #API Error Handling
        if response.status_code == 200:
            #Parse Data
            data = j.loads(response.text)
            
            #Check if random word is also contained in the dictionary API
            WordFoundString = DA(data[0])
            if WordFoundString == "True":
                WordFound == True
                return data[0]
        #API Down Block
        else:
            print("The API seems to be down, please try again later.")
            data = "Errors"
            return data
        