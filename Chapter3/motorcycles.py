motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#modify element 0 in a list
motorcycles[0] = 'ducati'
print(motorcycles)

#adding\appending elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducatti')
print(motorcycles)

# appending stuff to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting elements into a list with insert() method
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Remove elements from a list using a del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# you can remove any list element using it's index
# But If you use del, you won't be able to access the deleted value

del motorcycles[-1]
print(motorcycles)

# removing an Item in a list using the pop() method
# pop() method removes the last item in a list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Pop is useful for storing things
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# You can use pop() to remove any item by including the index number othe item you want to remove
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was {first_owned.title()}.")

# Removing an Item by value
# If you only know the value of the item you want to remove, you can use
# the remove() method.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

# You can use the remove() method to work with a value that's being removed
# from a list. Let's remove the value 'ducati' and print a reason for
# removing it from the list:

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Remember that the remove() method deletes ony the first occurrence of the
# value you specify. If there's a possibility the value appears more than
# once in the list, you'll need to use a loop to make sure all occurrences
# of the value are removed.

