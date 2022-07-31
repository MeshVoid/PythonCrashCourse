# Exercise 11-3 From the book Python Crash Course 2nd Edition by Erick Matthews

# Write a test case for Employee. Write two test methods, test_give_default
# _raise() and test_give_custom_raise(). Use the setUp() method so you don’t
# have to create a new employee instance in each test method. 
# Run your test case, and make sure both tests pass
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""
    def setUp(self):
        self.employee = Employee('Joshua', 'Cotter', 60000)

    def test_give_default_raise(self):
        """Test default salary raise function"""
        self.assertIn(str(self.employee.raise_salary()), '65000')
    
    def test_give_custom_raise(self):
        """Test custom salary amount raise function"""
        self.employee.raise_salary(3000)
        self.assertIn(str(self.employee.raise_salary()), '68000')


if __name__ == '__main__':
    unittest.main()