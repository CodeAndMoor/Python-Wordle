import requests as r
import json     as j

def CheckWord(word):
    #Word is Real Bool
    WordIsReal = True
    
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
        if "message" in data:
            WordIsRealString = "False"
        return WordIsRealString
    else:
        data = "Errors"
        return data