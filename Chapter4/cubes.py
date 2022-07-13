# Exercise 4-7. From the book Python Crash Course 2nd Edition by Erick Matthews

# Cubes: A number raised to the third power is called a cube. For example, the cube 
# of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the 
# cube of each integer from 1 through 10), and use a for loop to print out the value 
# of each cube.

cubes = []
for i in range(1,11):
    i = i**3
    cubes.append(i)
print(cubes)




# Exercise 4-9. Cube Comprehension: Use a list comprehension to generate a 
# list of the first 10 cubes.



cubes = [value**3 for value in range(1, 11)]
print(cubes)
