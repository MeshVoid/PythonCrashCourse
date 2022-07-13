# Exercise 6-5. From the book Python Crash Course 2nd Edition by Erick Matthews

# Rivers: Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'.

# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {'Volga':'Russia', 'Mississippi':'USA', 'Rhein':'Germany', 'Ili':'Kazakhstan'}

# proper and readable way to do it
for river, country in rivers.items():
    print(f"The {river} river runs through {country}")

print("\n")

# alternative janky\wrong way to do it
for river in rivers.items():
    print(f"{river[0]} runs through {river[1]}.")