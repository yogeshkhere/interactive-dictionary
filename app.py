import json 
from difflib import get_close_matches

#print(help(json.load))

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:
        return data [w.upper()]
    elif len(get_close_matches(w,data.keys())) >  0: #if we found any close match then in case this condition will apply
        yn =  input("Did you mean %s instead , Enter Y for yes and N for No " % get_close_matches(w,data.keys())[0])
    
        if yn == 'Y' or 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N' or 'n':
            return "The word doesn't exist,Please double check it"
        else:
            return "we didn't understand your entry"
    else:
        return "The word doesn't exist,Please double check it"


word = input("Enter Word: ")
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
