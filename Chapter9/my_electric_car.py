from electric_car import ElectricCar as EC # using alias EC

my_tesla = EC('tesla', 'Model Scam', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.increment_odometer(45)
my_tesla.read_odometer()