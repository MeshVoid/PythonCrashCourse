import json

filename = 'Chapter10/numbers.json' # file address
with open(filename) as file: # open the file in read mode
    numbers = json.load(file) # json.load() load the information stored in numbers.json and assign in to the variable names

[print(numbers)]