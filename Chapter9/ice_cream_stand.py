# Exercise 9-6. From the book Python Crash Course 2nd Edition by Erick Matthews

# Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class
# you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167).

# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.


class Restaurant:
    '''Resaurant class containing it's name and kitchen type,
    also can desribe itself and check if it's closed or not'''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Print a message with a brief restaurant information'''
        print(f"\nThe restaurant is called: {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} kitchen.")
        print(f"Yummy!")

    def open_restaurant(self):
        '''Print a message that the restaurant is open'''
        print(f"\nThe {self.restaurant_name} is open now.")


class IceCreamStand(Restaurant):
    """IceCreamStand class that inherits from a Restaurant class, represents aspects of an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'chocolate',
                        'pineapple', 'vanilla', 'mint']
    
    def display_flavors(self):
        print(f"The stand serves the following flavors:")
        for i in self.flavors:
            print(i)

ics = IceCreamStand("Freddie's frosty bits", "Ice cream stand")
ics.display_flavors()