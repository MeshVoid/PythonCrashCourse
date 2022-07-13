# Exercise 8-12. From the book Python Crash Course 2nd Edition by Erick Matthews

# Sandwiches: Write a function that accepts a list of items a person wants on a 
# sandwich. The function should have one parameter that collects as many items 
# as the function call provides, and it should print a summary of the sandwich 
# that’s being ordered. Call the function three times, using a different number 
# of arguments each time.

def make_sandwiches(*sandwich_topping):
    """Summarize the pizza we are about to make."""
    print("\nSandwiches ordered:")
    for entries in sandwich_topping:
        print(f"Sandwich with {entries}")

make_sandwiches('grilled cheese', 'turkey','ham')
make_sandwiches('grilled beefslices', 'turkey','ham', 'eggs')
make_sandwiches('grilled beefslices', 'chicken','ham', 'lamb ribs') 