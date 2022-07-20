# Exercise 10-4. From the book Python Crash Course 2nd Edition by Erick Matthews
#
# Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a
# file that stores all the responses.

class ProgrammingPoll:
    def __init__(self):
        self.file_name = 'Chapter10\programming_poll.txt'

    def intro_text(self):
        print(f"Hello there, we're conducting a poll.")
        print(f"Please spend a minute to answer 1 question!")

    def poll(self):
        poll = True
        while poll:
            user_answer = input("You love programming because: \n")
            with open(self.file_name, 'a') as self.file_object:
                self.file_object.write(f"{user_answer} \n")
            ask_continue = input("Do you wish to add new poll entry? y/n \n")
            if ask_continue.lower()[0] == 'y':
                poll = True
            else:
                print(f"Alright! All poll entries can be found here:")
                print(f"\t{self.file_name}")
                poll = False
                break


poll = ProgrammingPoll()
poll.intro_text()
poll.poll()