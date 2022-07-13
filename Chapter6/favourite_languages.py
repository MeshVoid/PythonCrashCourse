favourite_languages ={
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

#language = favourite_languages['sarah'].title()
#print(f"Sarah's favourite language is {language}.")

# using for loop instead:
'''
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")


for name in favourite_languages.keys():
    print(name.title())
'''

friends = ['phil', 'sarah']

for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# check if erin is still not in the list
if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

# use method sorted() to sort the keys out
print("\n")
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# using method value()
print("\nThe following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

# usign sets to avoid repetition:

print("\nThe following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

# Nesting a list inside a dictionary

favourite_languages ={
    'jen ':['python','ruby'],
    'sarah':['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python','haskell']
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
