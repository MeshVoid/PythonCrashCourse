# Exercise 9-1. From the book Python Crash Course 2nd Edition by Erick Matthews

# Restaurant: Make a class called Restaurant. The __init__() method for Restaurant
# should store two attributes: a restaurant_name and a cuisine_type.
#
# Make a method called describe_restaurant() that prints these two pieces of information, and a
# method called open_restaurant() that prints a message indicating that the
# restaurant is open. Make an instance called restaurant from your class.
# Print the two attributes individually, and then call both methods.

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


# Exercise 9-2. From the book Python Crash Course 2nd Edition by Erick Matthews

# Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() 
# for each instance.
'''
thai_restaurant = Restaurant('Oriental sun', 'thai')

thai_restaurant.describe_restaurant()
thai_restaurant.open_restaurant()

resto = Restaurant('Alfredo\'s bistro', 'awful')

resto.describe_restaurant()
resto.open_restaurant()

kz_restaurant = Restaurant("Lagmankhana Aksai", "central asian")
kz_restaurant.describe_restaurant()
kz_restaurant.open_restaurant()
'''