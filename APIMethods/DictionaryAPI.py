import requests as r
import json     as j

def CheckWord(word):
    #Variable Initialization
    WordIsRealString = "True" #Using a string here instead of a bool because sometimes we return the word Errors for if the API is down
    
    #Base URL of the Dictionary API
    BaseURL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    #request URL construction
    url = BaseURL + word

    #Results of the API response
    response = r.get(url)

    #API Error Handling
    if response.status_code == 200:
        #Parse Data
        data = j.loads(j.dumps(response.text))
        #Word Was not In Dictionary API
        if "message" in data:
            WordIsRealString = "False"
            return WordIsRealString
        #Word Was in Dictionary API
        return WordIsRealString
    #API Down Block
    else:
        Error = "Errors"
        return Error