# test_with_pytest.py

def test_always_passes():
    assert True


def test_always_fails():
    assert False


# def test_is_palindrome_empty_string():
#     assert is_palindrome("")


# File Naming Convention:

# Make sure your test file follows the Pytest naming convention. It should start with test_ or end with _test.py.
# In your case, the file is named test_example_fail.py,or test_pytest.py which should be fine.
# Test Function Naming:

# Ensure that your test function follows the Pytest naming convention. It should start with test_.
# In your case, the test function is named test_addition_fail, which is correct.
#  1 test for passing  just testing and another for failing below

def test_addition_pass():    #THE File name should start with test or end with _test.py 
    assert 2+2 == 4           # and also function name  should start with testss

# test_example_fail.py

def test_addition_fail():
    assert 2 + 2 == 5

#  u can also run your pytest files by directly running pytest command in terminal
#  ----or---

# Run the pytest command with the name of your test file:

# pytest test_example_pass.py