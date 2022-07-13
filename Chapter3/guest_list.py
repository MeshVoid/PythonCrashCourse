#guest_list.py
# Trying to stay vanilla with these exercises and not use for loops or
# functions
# Exercise 3-4. From the book Python Crash Course 2nd Edition by Eric Matthews
# If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

# Exercise 3-9. Use len() to indicate the overall number of guests invited to the party.

guest_list = ['Kelvin', 'Joao', 'Bill Paxton', 'Michael Jordan']

print(f"{guest_list[0]}, mate, you are invited to my party!")
print(f"{guest_list[1]}, dude, you are invited to my party!")
print(f"{guest_list[2]}, sir, you are invited to my party!")
print(f"{guest_list[3]}, I would be delighted to see you at my party!")
print(f"Number of guests invited to the party: {len(guest_list)}")

# Exercise 3-5. From the book Python Crash Course 2nd Edition by Eric Matthews
# Changing Guest List: You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
print('\n')
print(f"Sorry, {guest_list[2]} is not coming, we'll invite Billy Joel instead!")
guest_list[2] = 'Billy Joel'

print(f"{guest_list[0]}, mate, you are invited to my party!")
print(f"{guest_list[1]}, dude, you are invited to my party!")
print(f"{guest_list[2]}, sir, you are invited to my party!")
print(f"{guest_list[3]}, I would be delighted to see you at my party!")
print(f"Number of guests invited to the party: {len(guest_list)}")


# Exercise 3-6. From the book Python Crash Course 2nd Edition by Eric Matthews
# More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
print('\n')

guest_list.insert(0,'Myron')
guest_list.insert(3,'Metzger')
guest_list.append('Johnnie Bravo')

print(f"{guest_list[0]}, mate, you are invited to my party!")
print(f"{guest_list[1]}, dude, you are invited to my party!")
print(f"{guest_list[2]}, sir, you are invited to my party!")
print(f"{guest_list[3]}, I would be delighted to see you at my party!")
print(f"{guest_list[4]}, mate, you are invited to my party!")
print(f"{guest_list[5]}, dude, you are invited to my party!")
print(f"{guest_list[6]}, dude, you are invited to my party!")
print(f"Number of guests invited to the party: {len(guest_list)}")


# Exercise 3-7. From the book Python Crash Course 2nd Edition by Eric Matthews
# Shrinking Guest List: You just found out that your new dinner table won’t arrive 
# in time for the dinner, and you have space for only two guests.

print('\nSadly, I can only invite two people for dinner')
deleted_guest = guest_list.pop(0)
print(f"Sorry {deleted_guest}, I can only invite a limited amount of people")
deleted_guest = guest_list.pop(4)
print(f"Sorry {deleted_guest}, I can only invite a limited amount of people")
deleted_guest = guest_list.pop(3)
print(f"Sorry {deleted_guest}, I can only invite a limited amount of people")
deleted_guest = guest_list.pop(2)
print(f"Sorry {deleted_guest}, I can only invite a limited amount of people")
deleted_guest = guest_list.pop(2)
print(f"Sorry {deleted_guest}, I can only invite a limited amount of people")
print('\n')
print(f"{guest_list[0]}, mate, you are invited to my party!")
print(f"{guest_list[1]}, dude, you are invited to my party!")
print(f"Number of guests invited to the party: {len(guest_list)}")


del guest_list[0]
del guest_list[0]

print(guest_list)

