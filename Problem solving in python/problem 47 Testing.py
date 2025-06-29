"""
    This problem is about unit testing.
Your company needs a function that meets the following requirements:
For a given array of n integers, the function returns the index of the element with the minimum value in the array. If there is more than one element with the minimum value, it returns the smallest one.
If an empty array is passed to the function, it raises an exception. A colleague has written this method. The implementation in Python is listed below. Implementations in other languages can be found in the code template.
    """

# Function to find the minimum index
def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError(
            "Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

# Test data classes for different scenarios
class TestDataEmptyArray:
    @staticmethod
    def get_array():
        return []

# Static method to get the expected result
class TestDataUniqueValues:
    @staticmethod
    def get_array():
        return [3, 1, 4, 2, 5]
# Static method to get the expected result for unique values
    @staticmethod
    def get_expected_result():
        return 1

# Static method to get the expected result for exactly two different minimums
class TestDataExactlyTwoDifferentMinimums:
    @staticmethod
    def get_array():
        return [2, 1, 1, 3, 4]
# Static method to get the expected result for exactly two different minimums
    @staticmethod
    def get_expected_result():
        return 1

# Test cases for the minimum_index function
def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False

# If no exception is raised, the test fails
def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

# Test with exactly two different minimums
def TestWithExactlyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

# Run the tests
TestWithEmptyArray()
TestWithUniqueValues()
TestWithExactlyTwoDifferentMinimums()
print("OK")
