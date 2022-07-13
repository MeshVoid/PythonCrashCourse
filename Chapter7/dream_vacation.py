# Exercise 7-10. From the book Python Crash Course 2nd Edition by Erick Matthews

# Dream Vacation: 
# Write a program that polls users about their dream vaca-tion. 
# Write a prompt similar to If you could visit one place in the world, where 
# would you go? Include a block of code that prints the results of the poll.

user_answers = {} # declare empty dictionary

polling = True

while polling:
    add_entries = True

    name = input("\nWhat is your name? ")
    response = input("Which places would you like to visit someday? ")

    user_answers[name] = [response]
    
    while add_entries:
        repeat = input("Would you like to add a new entry? (yes/ no) ")
        if 'no' in repeat:
            break
        else:
            response = input("Which other places would you like to visit someday? ")
            user_answers[name] += [response]
            continue
            
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling = False
    

print("\n--- Poll Results ---")
for name, response in user_answers.items():
    print(f"\n{name} would like to visit:")
    for i in response:
        print(i)
