my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:] 
# this tells python to make a slice that starts at the first 
# and ends with the last item, making a copy of the list


# Copying the value without slicing won't create a separate list:
# THIS WON'T WORK!
# friend_foods = my_foods

my_foods.append('ravioli')
friend_foods.append('beshparmak')

print ('My favourite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
