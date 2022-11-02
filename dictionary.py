from difflib import get_close_matches
import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        print("Did you mean %s instead?" %get_close_matches(word, data.keys())[0])
        decide=input("y for yes. n for no. :")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("Not this word")
        else:
            return("You've pressed the wrong key")
    else:
        print("Word does not exist in this dictionary")

word = input("Enter word to search :")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
