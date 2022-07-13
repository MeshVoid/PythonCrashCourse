# names.py
# Exercise 3-1. From the book Python Crash Course 2nd Edition by Erick Matthews
# Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.
# gone a little bit over the top here, made a kill_list

hit_list = ['ruslan','shyako','maksutbek']
step = 1
to_kill = (len(hit_list))

def execute_targets():
    for i in hit_list:
        global to_kill
        print(f"I have just executed {i.title()}")
        print(f"There were {to_kill} names on the hit list.")
        print(f"{to_kill - step} more to go.")
        to_kill = to_kill - step


execute_targets()