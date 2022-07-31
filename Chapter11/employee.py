# Exercise 11-3 From the book Python Crash Course 2nd Edition by Erick Matthews

# Employee: Write a class called Employee. The __init__() method should take 
# in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5,000 to 
# the annual salary by default but also accepts a different raise amount.

# Write a test case for Employee. Write two test methods, test_give_default
# _raise() and test_give_custom_raise(). Use the setUp() method so you don’t
# have to create a new employee instance in each test method. 
# Run your test case, and make sure both tests pass


class Employee:
    """Class to store employee information"""

    def __init__(self, first_name, last_name, annual_salary):
        """Employee default info"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def raise_salary(self, raise_amount=5000):
        """Raise employee's annual salary to a certain amount"""
        self.annual_salary += raise_amount
        return self.annual_salary

    def show_employee_details(self):
        """Print employee details (name, salary)"""
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Salary: {self.annual_salary}")