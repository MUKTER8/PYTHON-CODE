"""Type Conversion
Type Conversion is the conversion of object from one data type to another data type. 
Implicit Type Conversion is automatically performed by the Python interpreter. 
Python avoids the loss of data in Implicit Type Conversion. 
However, Explicit Type Conversion is also called Type Casting, the data types of object are converted using predefined function by user. 
In Type Casting, loss of data may occur as we enforce the object to specific data type."""
a =2 
b = 3.5
c= int("4")

sum = a+b-c
print(sum)

num1=3.1416
print(type(num1))
num1=str(num1)
print(type(num1))