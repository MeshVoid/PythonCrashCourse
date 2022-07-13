# Define tuple with ()

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# This will cause error, because tuples are immutable:
# dimensions[0] = 250


# you can loop through all values in a tuple:
for dimension in dimensions:
    print(dimension)


# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.

print("\n")

dimensions = (200, 50)
print("Original dimension:")
for dimension in dimensions:
    print(dimension)



dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)