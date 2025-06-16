# Define the Difference class to calculate maximum absolute difference
class Difference:
    def __init__(self, a):
        # Store the list of integers as a private variable
        self.__elements = a
        # Initialize maximumDifference to 0
        self.maximumDifference = 0

    # Method to compute the maximum absolute difference between any two elements
    def computeDifference(self):
        # Maximum difference is the difference between max and min elements
        self.maximumDifference = max(self.__elements) - min(self.__elements)

# ---------------- Main Program ----------------

# Read and ignore the first input (number of elements), not needed in Python
_ = input()

# Read the list of integers from input
a = [int(e) for e in input().split(' ')]

# Create an instance of the Difference class
d = Difference(a)

# Call the method to compute the maximum difference
d.computeDifference()

# Print the computed maximum difference
print(d.maximumDifference)
