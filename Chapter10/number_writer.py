import json

numbers = [1, 3, 5, 7, 11, 13]

filename = 'Chapter10/numbers.json' # we choose a filename to store the numbers.
with open(filename, 'w') as f: # We open the file in write mode, which allows json to write data to the file.
    json.dump(numbers, f) # we use json.dump() function to store the list numbers in the file numbers.json