import pizza_module  # import the whole module
from pizza_module import make_pizza  # importing just a function to our file
from pizza_module import make_pizza as mp # giving an alias name to the function make_pizza
import pizza_module as pm # giving an alias to the whole pizza_module
from pizza_module import * # import all functions in a module

pizza_module.make_pizza(14, 'pepperoni')
pizza_module.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')


make_pizza(14, 'pepperoni')  # no need for pizza_module. now!
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')


mp(14, 'pepperoni')  # now it's a short name mp
mp(16, 'mushrooms', 'green peppers', 'extra cheese')


pm.make_pizza(14, 'pepperoni')  # now it's a short name mp
pm.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
