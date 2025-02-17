#Learn Tuples in Python, a tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#Create a Tuple: A tuple is created by placing all the items (elements) inside round brackets (), separated by commas.
#Syntax: tuple1 = ("apple", "banana", "cherry")

tup=("apple","banana","cherry")
print(tup[1]) #banana
print(type(tup)) #<class 'tuple'>

#Tuple Slicing: You can return a range of items by using the slice syntax.
print(tup[0:2])

#Tuple Methods is used to add items in a tuple
#Syntax: tuple1 = ("apple", "banana", "cherry")
tup1=(1,2,3,4,1,1,1,1)

print(tup1.index(2)) #index() method returns the index of the specified element in the tuple.
print(tup1.count(1)) #count() method returns the number of times a specified value occurs in a tuple.