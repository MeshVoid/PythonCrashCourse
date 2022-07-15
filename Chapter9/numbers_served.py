# Exercise 9-4. From the book Python Crash Course 2nd Edition by Erick Matthews

# Number Served: Start with your program from Exercise 9-1 (page 162). Add an
# attribute called number_served with a default value of 0. Create an instance
# called restaurant from this class. Print the number of customers the 
# restaurant has served, and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number of 
# customers that have been served. Call this method with a new number and print
# the value again. Add a method called increment_number_served() that lets you
# increment the number of customers who’ve been served. Call this method with 
# any number you like that could represent how many customers were served in, 
# say, a day of business.


class Restaurant:
    '''Resaurant class containing it's name and kitchen type,
    also can desribe itself and check if it's closed or not'''

    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        '''Print a message with a brief restaurant information'''
        print(f"\nThe restaurant is called: {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} kitchen.")
        print(f"Yummy!")
        print(f"Currently served {self.number_served} clients.")

    def open_restaurant(self):
        '''Print a message that the restaurant is open'''
        print(f"\nThe {self.restaurant_name} is open now.")

    def set_number_served(self, number):
        '''Sets the number of customers 
        served by the restaurant.'''
        self.number_served = number

    def increment_number_served(self, number):
        '''Increments the number of people served'''
        self.number_served += number
    

restaurant = Restaurant('Frankie\'s finger chops', 'grilled insects', 45)

restaurant.describe_restaurant()
restaurant.set_number_served(12)
restaurant.describe_restaurant()
restaurant.increment_number_served(34)
restaurant.describe_restaurant()
