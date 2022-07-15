# define a class called Dog (By convention, captilized names refer to classes in Python)
class Dog:
    """A simple attempt to model a dog."""  # docstring describing what this class does

    # Python runs __init__() automatically when we create, notice self!
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name  # variable with self. are available to every method in the class and it's instances
        self.age = age  # Variables that are accessible through instances like this are called attributes

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()

print(f"\nMy dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()