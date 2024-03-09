# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
# from datastructures.array import Array
import sys
sys.path.append('C:\Users\atmen\Downloads\cs152-assignments-repo-Nicos10517-main\cs152-assignments-repo-Nicos10517-main\datastructures')
from datastructures.array import Array
class TestClassTemplate:
    def test_method_template(self):
        # Arrange (set up your test data)
        length = 4
        test_data = [1, 2, 3, 4]

        # Act (perform the action you want to test)
        test_array = array('i', test_data)
        # Assert (check that the test is passing)
        assert len(test_array) == length, "Test Failed: Array length does not match expected value."
        for i, value in enumerate(test_data):
            assert test_array[i] == value, f"Test Failed: Element {i} does not match expected value."

test_instance = TestClassTemplate()
test_instance.test_method_template()
print("Hurray!")