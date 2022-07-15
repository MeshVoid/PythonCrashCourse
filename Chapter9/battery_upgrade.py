# Exercise 9-9. From the book Python Crash Course 2nd Edition by Erick Matthews

# Battery Upgrade: Use the final version of electric_car.py from this section.

# Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 100
# if it isn’t already. Make an electric car with a default battery size,
# call get_range() once, and then call get_range() a second time after
# upgrading the battery. You should see an increase in the car’s range.


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 31

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): 
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery: # Defining a separate class for a Battery
    """ A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """Check battery size and set the capacity to 100"""
        if self.battery_size != 100: 
            self.battery_size = 100
            print("The battery has been upgraded to a 100-kwh battery.")



# This method should check the battery size and set the capacity to 100
# if it isn’t already. Make an electric car with a default battery size,
# call get_range() once, and then call get_range() a second time after
# upgrading the battery. You should see an increase in the car’s range.

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery() # <- instance of a class Battery used here



    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


tesla_car = ElectricCar('Tesla Trash', 'Model Scam', '2022')
print(tesla_car.get_descriptive_name())
tesla_car.battery.describe_battery()
tesla_car.battery.get_range()
tesla_car.battery.upgrade_battery()
tesla_car.battery.describe_battery()
tesla_car.battery.get_range()