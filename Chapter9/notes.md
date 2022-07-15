# Chapter 9

# CLASSES

**_Object-oriented programming (OOP)_** is one of the most effective approaches to writing software.
In OOP you write **_classes_** that represent real-world things and situations, and you create **_objects_** based on these **_classes_**. When you write a class, you define the general behavior that a whole category of objects can have.

When you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire. 

Making an object from a class is called **_instantiation_**, and you work with **_instances_** of a class. Understanding logic behind classes trains you to think logically so you can write programs that effectively address almost any problem you encounter.

## Creating and using a class

You can model almost anything using classes. Let's create class called dog as an example. It will store a name, age and functions like sit() and roll_over()

```python
# define a class called Dog (By convention, captilized names refer to classes in Python)
class Dog:
    """A simple attempt to model a dog."""  # docstring describing what this class does

    # Python runs __init__() automatically when we create, notice self!
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name  # variable with self. are available to every method in the class and it's instances
        self.age = age  # Variables that are accessible through instances like this are called attributes

    def sit(self):
        # Because these methods don’t need additional information to run, 
        # we just define them to have one parameter, self.
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```
## The __ init __() method
You can notice the '\__init__ ()' method in the example above. It is a special method that Python runs automatically whenever we create a new instance based on the class. This method has two leading underscores and two trailing underscores to help Python prevent conflicting with your own method names.

Make sure you follow the syntax of underscores, otherwise Python will return an error.

In the example above we define the \__init__() method to have three parameters: self, name and age

**Self** parameter is required in the init method definition, and it must come first before the other parameters. When we make an instance of Dog, Python will call the \__init__() method from the Dog class. We’ll pass Dog() a name and an age as arguments; self is passed automatically, so we don’t need to pass it. Whenever we want to make an instance from the Dog class, we’ll provide values for only the last two parameters, name and age.

## Making an instance from a class

Think of a class as a set of instructions for how to make an instance. The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs.

```python
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

The naming convention is helpful here: we can usually assume that a capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.

### **Accessing attribultes**
> my_dog.name

Dot notation is used often in Python. This syntax demostrates how Python finds an attribute's value. Here python finds the attribute _name_ associated with _my\_dog_.

### **Calling Methods**
```python
my_dog.sit()
my_dog.roll_over()
```
To call a method, give the name of the instance (in this case, my_dog) and the method you want to call, separated by a dot. When Python reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code. 

### **Creating Multiple instances**

```python
my_dog = Dog('Willie', 6) # creating a first instance of the class
your_dog = Dog('Lucy', 3) # creating a second instance of the class

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()

print(f"\nMy dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()
```
You can make as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.

## Working with classes and instances

You can use classes to represent many real-world situations, once you have written a class you will spend most of your time working with instances created from that class. 

One of the first tasks you'll want to do is modify the attributes that are associated with a particular instance of a class. You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

### **The car class**

Let take a look at an example car class:
```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
```

## Setting a default value for an attribute

When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the \__init__() method, where they are assigned a default value.

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0 # setting a default value for an attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self): # adding new method
        """Print a statement showing the car's mileage."""
        print(f"\nThis car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer() # calling read_odometer function
```
This time when Python calls the __init__() method to create a new instance, it stores the make, model, and year values as attributes like it did in the previous example. Then Python creates a new attribute called odometer_reading and sets its initial value to 0.

Not many cars are sold with exactly 0 miles on the odometer, so we need a way to change the value of this attribute.

## Modifying attribute values

You can change an attribute's value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method. Let's look at each of these approaches.

## Modifying an attribute's value directly

The simplest way to modify the value of an attribute is to access the attribute directly through an instance.
```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0 # setting a default value for an attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self): # adding new method
        """Print a statement showing the car's mileage."""
        print(f"\nThis car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


my_new_car.odometer_reading = 23 # modifying the attribute directly
my_new_car.read_odometer() # calling read_odometer function
```
Sometimes you’ll want to access attributes directly like this, but other times you’ll want to write a method that updates the value for you.


## Modifying an attribute's value through a method

It can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0 # setting a default value for an attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self): # adding new method
        """Print a statement showing the car's mileage."""
        print(f"\nThis car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): # method we use to modify attribute's value
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


my_new_car.update_odometer(34) # modifying attribute through a method
my_new_car.read_odometer() # calling read_odometer function
```

We can extend the method update_odometer() to do additional work every time the odometer reading is modified. Let’s add a little logic to make sure no one tries to roll back the odometer reading:

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 31 # setting a default value for an attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self): # adding new method
        """Print a statement showing the car's mileage."""
        print(f"\nThis car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): # method we use to modify attribute's value
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


my_new_car.read_odometer() # calling read_odometer function
my_new_car.update_odometer(0) # modifying attribute through a method
```

## Incrementing an attribute's value through a method

Sometimes you'll want to increment an attribute's value by a certain amount rather than set an entirely new value. 

Example of a method that llows us to pass an incremental amount and add that value to the odoemter reading:

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 31 # setting a default value for an attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self): # adding new method
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): # method we use to modify attribute's value
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles): # adding a new method to increment an attribute
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


my_new_car.read_odometer() # calling read_odometer function
my_new_car.update_odometer(0) # modifying attribute through a method


my_used_car = Car('subaru', 'forester', 1998)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```
The new method increment_odometer() takes in a number of miles and adds this value to self.odometer_reading.

_You can use methods like this to control how users of your program update values such as an odometer reading, but anyone with access to the program can set the odometer reading to any value by accessing the attribute directly. Effective security takes extreme attention to detail in addition to basic checks like those shown here._


# Inheritance

You don't always have to start from scratch when writing a class. If the class you're writing is a specialized version of another class you wrote, you can use **_inheritance._**

When one class **_inherits_** from another, it takes on the attributes and methods of the first class. The original class is called the parent class, and the new class is the **_child class._**

The child class can inherit any or all of the attributes and methods of its parent class, but it's also free to define new attributes and methods of its own.

## The \__init__() method for a child class

When you're writing a new class based on an existing class, you'll often want to call the \__init__() method from the parent class. This will initialize any attributes that were defined in the parent \__init__() method and make them available in the child class.

Example:
```python
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

    def read_odometer(self): # adding new method
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

class ElectricCar(Car): # inherts from parent Car class
    # it appears after Car class in the file so that it could inherit from it
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(manufacturer, model, year) # super() is a special method that allows us to use methods from the parent Car class
    
my_bmw = ElectricCar('BMW', "iX", 2023)
print(my_bmw.get_descriptive_name())
```

We write down our child class after the parent class with the following syntax:
> class ClassName(ParentClass):

Then we define the \__init__() method, and use a **_super().\__init\__()** method. The _**super()**_ function is a special function that allows you to call a method from the parent class. This line tells Python to call the \__init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method.

The name _super_ comes from a convention of calling the parent class a _superclass_ and the child class a _subclass_.

## Defining attributes and methods for the child class

Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.

Let's add an attribute that's specific to electric cars (a battery, for example) and a method to report on this attribute. We'll store the battery size and write a method that prints a description of the battery:

```python
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
        self.battery_size = 75 # adding new attribute with a default value to child class

    def describe_battery(self): # defining method in a child class
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
my_bmw = ElectricCar('BMW', "iX", 2023)
print(my_bmw.get_descriptive_name())
my_bmw.describe_battery() # calling a method of a child class
```

There's no limit to how much you can specialize the Child class. You can add as many attributes and methods as you need to it. 

## Overriding methods from the parent class

You can override any method from the parent class that doesn't fit what you're trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.

```python
class ElectricCar(Car):
    """"""

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
```

Now if someone tries to call fill_gas_tank() with an **ElectricCar** class, Python will ignore the method fill_gas_tank() in **Car** parent class and run this code instead. 

_When you use inheritance, you can make your child classes retain what you need and override anything you don't need from the parent class._

## Instances as attributes

When you're writing a real world program, you may stumble upon a situation when you're adding more and more detail to your class. You'll find that you have written a large list of attributes and methods and that your files are becoming lengthier and lengthier. 

If your class is getting to long you can consider breaking your large class into smaller class that work together.

For example, if we continue adding more and more detail to our **ElectricCar** class, we might notice that we're adding many attributes and methods specific to the car's battery. When we see this happening, we can stop and move those attributes and methods to a separate class called **Battery**. Then we can use a Battery instance as an attribute in the ElectricCar class:

```python
class Battery: # Defining a separate class for a Battery
    """ A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery() # <- instance of a class Battery used here

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
    

my_bmw = ElectricCar('BMW', "iX", 2023)
print(my_bmw.get_descriptive_name())
my_bmw.battery.describe_battery() # <- running a method from the class battery
```

This looks like a lot of extra work, but now we can describe the battery in as much detail as we want without cluttering the ElectricCar class. Let's add another method to Battery that reports the range of the car based on the battery size:

```python
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

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery() # <- instance of a class Battery used here

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


my_bmw = ElectricCar('BMW', "iX", 2023)
print(my_bmw.get_descriptive_name())
my_bmw.battery.describe_battery() # running a method from the class battery
my_bmw.battery.get_range()
my_bmw.fill_gas_tank()
```


## Modeling real-world objects

As you begin to model more and more complicated things with your code, like the one we have writtern above, you will start asking yourself interesting questions. 

Is the range of an electric car a property of the battery of the car? If we're only describing one car, it's probably fine to maintain the associataion of the method **_get_range()_** with the Battery class. 

But if we’re describing a manufacturer’s entire line of cars, we probably want to move get_range() to the ElectricCar class. The get_range() method would still check the battery size before determining the range, but it would report a range specific to the kind of car it’s associated with. Alternatively, we could maintain the association of the get_range() method with the battery but pass it a parameter such as car_model. The get_range() method would then report a range based on the battery size and car model.

When you ask yourself questions like this you're already thinking at a higher logical level rather than a syntax-focused level. You're thinking not about Python, but about how to represent the real-world in code. When you reach this point, you'll realize there are often no right or wrong approaches to modeling real-world situations.

If your code is working as you want it to, you’re doing well! Don’t be discouraged if you find you’re ripping apart your classes and rewriting them several times using different approaches. In the quest to write accurate, efficient code, everyone goes through this process.