import requests as r
import json     as j

#Gets a random, five letter word from an API
def GetWord():
    #URL for the API response
    url = "https://random-word-api.herokuapp.com/word?length=5"
    
    #Results of the API response
    response = r.get(url)

    #API Error Handling
    if response.status_code == 200:
        #Parse Data
        data = j.loads(response.text)
        return data[0]
    else:
        data = "Error"
        