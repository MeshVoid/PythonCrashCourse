# Chapter 11

# Testing your code

When you write a function or a class, you can also write tests for that code. Testing proves that your code works as it's suposed to it in response to all the input types it's designed to receive. Every programmer makes mistakes, so every programmer must test their code often, catching problems before users encounter them.

To test your code using tools in Python one must write *_unittests_*. 

## Testing a function

To learn about testing we need to code a test. Here's a simple example:

```python
#name_function.py
def get_formatted_name(first, last): # first, last name as attribute
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}" # assign to full_name
    return full_name.title() # return full name with space in title format
```
We will use the following separate program to import the function and assign and print values:
```python
#names.py
from name_function import get_formatted_name # importget_formatted name function from a different file

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}.")
```
_The code above runs smoothly and outputs correcly, but if we were to change the get\_formatted\_name() function so that it could also handle middle names, we want to make sure we don't break things along the way. Not to test things manually we could automate the testing of a function's output._

## Unit Test and Test Cases

The module _**unittest**_ from the Python standard library provides tools to test your code. A _unit test_ verifies that one specific aspect of a function's behavior is correct. A _test case_ is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations you expect it to handle. A good test case considers all the possible kinds of input a function could receive and includes a full range of unit tests covering all the possible ways you can use a function.

It's good enough to write tests for your code's critical behaviors and then aim for full coverage only if the project starts to see widespread use.

## A passing test

The syntax for setting up a test case takes some getting used to, but once you've set up the test case it's straightforward to add more unit tests for your functions.

Here's a test case with one method that verifies that the function get_formatted_name() works correctly when given a first and last name:

```python
# test_name_function.py
import unittest # 1
from name_function import get_formatted_name # 2

class NamesTestCase(unittest.TestCase): # 3
    """Tests for 'name_function.py'"""
    
    def test_first_last_name(self): 
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin') # 4
        self.assertEqual(formatted_name, 'Janis Joplin') # 5

if __name__ == '__main__': # 6
    unittest.main()
```
* 1- Importing unittest module 
  
* 2- Importing get_formatted_name function from name_function file
  
* 3- Create a class called NamesTestCase, which will contain a series of unit tests for get_formatted_name() method. This class must inherit from the class unittest.TestCase, so Python knows how to run the tests you write. NamesTestCase contains a single method _test\_first\_last\_name(self)_ because we're verifying that names with only a first and last name are formatted correctly. Every method that starts with _**test\_**_ will be run **automatically** when we run test_name_function.py. 

* 4- In this example we call get_formatted_name() method within that test function with the arguments 'janis' and 'joplin', and assign the result to formatted_name.

* 5- We use **unittest**'s most useful feature: an **_assert_** method. Assert method verify that a result you received matches the result you expected to receive. In this case, because we know get_formatted_name() is supposed to return a capitalized, properly spaced full name, we expect the value of formatted_name to be Janis Joplin. To check if this is true, we use unittest's assertEqual() method and pass it formatted_name and 'Janis Joplin' as arguments. Basically we say -> Compare the value in formatted_name to == 'Janis Joplin'. If they are equal, it's all good, if not, let me know!

* 6- When a file is imported, the interpreter executes the file as it's being imported. The if block here looks at a special variable, _\_\_name\_\__, which is set when the program is executed. If this file is being run as the main program, the value of _\_\_name\_\__ is set to '_\_\_main\_\__' and this block will not be executed. 

## A failing test

What does a failing test look like? Let's modify get_formatted_name() so it can handle middle names, but it will also break the function for names with just a first and last names:

```python
# name_function.py
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

When we test this get_formatted_name() with our test_name_function.py we will get an error:

```python
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "MatthesPythonCrashCourse\Chapter11\test_name_function.py", line 9, in test_first_last_name
    formatted_name = get_formatted_name('janis','joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

E - here stands for error. Next we see that error is caused by the function test_first_last_name() in NamesTestCase class. We can see the that get_formatted_name() no longer works because it's missing a required positional argument: 'last'

## Responding to a failed test

What do you do when a test fails? When a test fails, don't change the test. Instead, fix the code that caused the test to fail.

Let's make modifications, so that our test would pass:
```python
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

Now our test runs fine.


## Adding new test

To add new tests, to check middle names, for example, we would add another method to the class NamesTestCase:
```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self): # new method to check middleneames
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
```

## Testing a class

Python provides a number of assert methods in the _**unittest.TestCase**_ class. You can use these methods only in a class that inherits from _**unittest.TestCase**_. Here's the table with some methods available rom the unittest Module:


Method | Use|
---------|----------|
 assertEqual(a,b) | Verify that a -- b | 
 assertNotEqual(a,b) | Verify that a !- b | 
 assertTrue(x) | Verify that x is True |
 assertFalse(x) | Verify that x is False| 
 assertIn(item, list) | Verify that _item_ is in list| 
 assertNotIn(item, list) | Verify that _item_ is not in list| 


## A Class to test

Testing a class is similar to testing a function - much of your work involves testing the behavior of the methods in the class. But there are a few differences, so let's write a class to test. Consider a class that helps administer anonymous surveys:

```python
#survey.py
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question): # 1
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self): # 2
        """Show the survey question."""
        print(self.question)
    
    def store_response(self,new_response): # 3
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self): # 4
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```
* 1 - This class starts with a survey question you provide and includes an empty list to store responses.
* 2 - Method to print the survey question
* 3 - Add a new response to the list responses.
* 4 - Print all the responses from the list responses.

To show how this class works let's write a program:
```python
#language_survey.py
from survey import AnonymousSurvey

# Define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```
_This program defines a question ("What language did you first learn to speak?") and creates an AnonymousSurvey object with that question. The program calls show_question() to display the question and then prompts for responses. Each response is stored as it is received. When all responses have been entered (the user inputs q to quit), show_results() prints the survey results._

This class works perfectly for a simple anonymous survey. But let's say we want to improve AnonymousSurvey and the module it's in, _**survey**_. We could allow each user to enter more than one response. 

To ensure that we don't break existing behavior as we develop this module, we can write tests for the class.

## Testing the AnonymousSurvey class

Let's write a test using the assertIn() method to verify that the response is in the list of responses after it's been stored:
```python
#test_survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase): # 1
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self): # 2
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question) # 3
        my_survey.store_response('English')
        self.assertIn("English", my_survey.responses) # 4

if __name__ == '__main__':
    unittest.main()
```
* 1- We call our test case TestAnonymousSurvey that inherits from unittest.TestCase.
* 2- The first method will verify that when we store a response to the survey question, the response ends up in the survey's list of responses. A good descriptive name for this method is test_store_single_response(). If this test fails, we'll know from the method name shown in the output of the failing test that there was a problem storing a single response to the survey.
* 3- we make an instance called my_survey with the survey question and store it using the store_response()method. 
* 4- We verify that the response was stored correcly by asserting that English is in the listy my_survey.responses

Let’s verify that three responses can be stored correctly. To do this, we add another method to TestAnonymousSurvey:
```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn("English", my_survey.responses)
    
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin'] # 1
        for response in responses: # 2
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

* 1- We call the new method test_store_three_responses(). We create a survey object just like we did in test_store_single_response(). We define a list containing different responses.
* 2- Then we call store_response() for each of these responses. Once the responses have been stored, we write another loop and assert that each reponse is now in my_survey.responses.

## The setUp() method

This works perfectly. However, these tests are a bit repetitive, so we’ll use another feature of unittest to make them more efficient. The _**unittest.TestCase**_ class has a _**setUp()**_ method that allows you to create these objects once and then use them in each of your test methods. When you include a _**setUp()**_ method in a TestCase class, Python runs the _**setUp()**_ method before running each method starting with **_test\__**.

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question) # 1
        self.responses = ['English','Spanish','Mandarin'] # 2

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
 
if __name__ == '__main__':
    unittest.main()
```
* 1- The method setUp() does two things: it creates a survey instance,
* 2- and it creates a list of responses.
* Each of these is prefixed by self, so they can be used anywhere in the class. This makes the two test methods simpler, because neither one has to make a survey instance or a response. The method test_store_single_response() verifies that the first response in self.responses-self.responses[0]-- can be stored correctly, and test_store_three_responses() verifies that all three resopnses in self.resopnses can be stored correctly.

