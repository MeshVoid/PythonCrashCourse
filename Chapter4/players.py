# The way slicing works in Python

players = ['charles','martina','michael','florence','eli']

print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

# You can use a slice in a for loop if you want to loop through a subset of elements in a list.

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())