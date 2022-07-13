# Exercise 5-8. From the book Python Crash Course 2nd Edition by Erick Matthews

# Hello Admin: Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after
# they log in to a website. Loop through the list, and print a greeting to each user:

# If the username is 'admin', print a special greeting, such as Hello admin, would you
# like to see a status report?• Otherwise, print a generic greeting, such as Hello Jaden,
# thank you for logging in again.

usernames = ['admin', 'mike', 'raul', 'paul', 'alexander']

username = 'admin'

if username in usernames:
    print(f"\nHello there, {username.title()}! Welcome to the nuclear warhead control system!")

for username in usernames:
    print(f"Hello there, {username.title()}! Welcome to the control system!")

# Exercise 5-9. From the book Python Crash Course 2nd Edition by Erick Matthews

# No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.

print("\n")
usernames =[]
if usernames:
    if user in usernames:
        print(f"\nHello there, {username.title()}! Welcome to the nuclear warhead control system!")
    for user in usernames:
        print(f"\nHello there, {username.title()}! Welcome to the control system!")
else:
    print("We need users in our database!")

# Exercise 5-10. From the book Python Crash Course 2nd Edition by Erick Matthews

# Checking Usernames: Do the following to create a program that simulates how websites ensure 
# that everyone has a unique username.

# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or two of the new 
# usernames are also in the current_users list.
# 
# • Loop through the new_users list to see if each new username has already been used. 
# If it has, print a message that the person will need to enter a new username. 
# If a username has not been used, print a message saying that the username is available.
# 
# • Make sure your comparison is case insensitive. If 'John' has been used, 
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users 
# containing the lowercase versions of all existing users.)

print("\n")

current_users = ['admin', 'mike', 'raul', 'paul', 'alexander']
new_users = ['charles', 'Mike', 'lilly', 'chingiz', 'tyrone', 'ALEXander']

for users in new_users:
    if users.lower() in current_users:
        print(f"\nYou can't take the name {users}, it's already taken!")
        print(f"You will have to choose a different name!")
    if users.lower() not in current_users:
        print(f"\nUsername {users} is available!")
