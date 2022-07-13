squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# more concise way to write this code:

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# list comprehension allows you to generate the same list in just one line of code.
squares = [value**2 for value in range(1, 11)]
print(squares)
