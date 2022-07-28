import json

file_name = "Chapter10/username.json"

with open(file_name) as file:
    username = json.load(file) # user json.load() to read info in username.json
    print(f"Welcome back, {username}!") # welcome user
