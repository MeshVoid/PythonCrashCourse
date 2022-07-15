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

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
    
my_bmw = ElectricCar('BMW', "iX", 2023)
print(my_bmw.get_descriptive_name())
my_bmw.describe_battery()
my_bmw.fill_gas_tank()