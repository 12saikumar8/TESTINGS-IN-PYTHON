# Here we are testing with use of unit tests
#  You might want to write one test that always passes and one that always fails:


# test_with_unittest.py

import unittest

class TryTesting(unittest.TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()


# Here's an example of a passing test:
# below

import unittest
class TestPassingExample(unittest.TestCase):
    def test_addition(self):
        result = 2 + 3
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

# and here for failing test


import unittest

class TestFailingExample(unittest.TestCase):
    def test_subtraction(self):
        result = 5 - 3
        # The following assertion will fail, as the result is not equal to 5
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()


#     Run Tests Using Command Line:
# Open a terminal or command prompt, navigate to the directory containing your test script, and run the following command:

# python -m unittest <your_test_module>
# Replace <your_test_module> with the name of your test script without the ".py" extension. For the example above, you would run:

# for example
# python -m unittest Unit_tests here Unit_tests is your file name 
# This will discover and run all the test cases in the specified module.
