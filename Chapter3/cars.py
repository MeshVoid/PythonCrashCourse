# sort() method to sort the list in alphabetical order
# sort() method - permanently changes the list order
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.sort()
print(cars)

# you can use argument reverse = True in sort()
cars.sort(reverse=True)
print(cars)

# Use sorted() function to display list in order but not
# change it permanently
cars = ['bmw','audi','toyota','subaru']
print("\n Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

# to reverse the original order of the list you can use
# reverse() method
print("\n")
print(cars)
cars.reverse()
print(cars) 
# Notice that reverse() doesn't sort backward alphabetically;
# it just reverses the order of the list!
# reverse() changes the list permanently, but you cal revert to the 
# original order anytime by applying reverse() to the same list a second time.

# You can quickly find the length of a list by using len() function.abs(x)

cars = ['bmw','audi','toyota','subaru']
print(len(cars))

