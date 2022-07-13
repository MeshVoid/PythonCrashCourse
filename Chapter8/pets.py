
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'william')

# the order of positional arguments is important
describe_pet('harry', 'hamster')

# Using keyword arguments

describe_pet(animal_type='hamster', pet_name='harry')

# using default values in function definition

def describe_pet(pet_name, animal_type ='dog'): # order of parameters has to be changed
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='Larry')
