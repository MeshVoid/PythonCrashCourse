# Exercise 11-1 From the book Python Crash Course 2nd Edition by Erick Matthews

# Create a file called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want to
# test). Write a method called test_city_country() to verify that calling your
# function with values such as 'santiago' and 'chile' results in the correct
# string. Run test_cities.py, and make sure test_city_country() passes

import unittest
from city_functions import city_functions

class TestCityFunctions(unittest.TestCase):
    """Test city functions"""
    def test_city_functions(self):
        city_data = city_functions('santiago', 'chile')
        self.assertEqual(city_data, 'Santiago, Chile')

    def test_city_with_population_function(self):
        city_data = city_functions('moscow', 'russia', '10000000')
        self.assertEqual(city_data, 'Moscow, Russia - population: 10000000')

if __name__ == '__main__':
    unittest.main()
