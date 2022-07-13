# Let's use a for loop to print out each name in a list:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print("\n")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

print("\nThank you,everyone. That was a great magic show!")
