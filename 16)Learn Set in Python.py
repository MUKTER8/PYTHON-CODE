"""
Learn Set in Python, a set is a collection of unique elements.Example:set= {1,2,3,4,5}
"""
collection = {1, 2, 3, 4, 5, 2, "a", "b", "c","d"}  # Set is a collection of unique elements
print("Output 1:", collection)
print("Output 2:", type(collection))
print("Output 3:", len(collection))

my_set = set()  # Empty set
print("Output 4:", my_set)

my_set.add(1)  # Add element to set
my_set.add(2)
print("Output 5:", my_set)
my_set.remove(1 )  # Remove element from set
print("Output 6:", my_set)

print("Output 7:", 7 in my_set)  # Check if element is in set

  # Remove element from set
print("Output 8:", (collection.pop()))
print("Output 9:", collection)

print("Output 10:",my_set.clear())  # Clear set

set1={1,2,3,4,5}
set2={4,5,6,7,8}
print("Output 11:",set1.union(set2))  # Union of two sets
print("Output 12:",set1.intersection(set2))  # Intersection of two sets
print("Output 13:",set1.difference(set2))  # Difference of two sets
print("Output 14:",set2.intersection(set1))  # Symmetric difference of two sets