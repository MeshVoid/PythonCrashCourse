# Exercise 4-12. From the book Python Crash Course 2nd Edition by Erick Matthews

# All versions of foods.py in this section have avoided using for loops when printing to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:] 

my_foods.append('ravioli')
friend_foods.append('beshparmak')

print ('My favourite foods are:')
for i in my_foods:
    print(i)

print("\nMy friend's favorite foods are:")
for i in friend_foods:
    print(i)

