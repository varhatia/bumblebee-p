import json
import difflib

from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("./files/data.json"))

def translate(w) :

    w =  w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        response = input("Word doesn't exist. Suggest to try this: %s . Press Y to continue or N instead " % get_close_matches(w, data.keys())[0])
        if (response.lower() == "y"):
            return data[get_close_matches(w, data.keys())[0]]
        elif (response.lower() == "n"):
            return "The word doesn't exist. Please recheck it"
        else:
            return "We do not understand your ask"
    else:
        return "Word doesn't exist. Please try again"

word = input("Enter word: ")

output = translate(word)
if(type(output) == list):
    for item in output:
        print(item)
else:
    print(output)
