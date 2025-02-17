#practice list and tuples
#1.Write  a program as k the user  to enter names of their favorite 3 fruits and store them in a list called fruits.
"""
#Solve :First way
fruits = []
f1 = input("Enter the 1st favorite fruits: ")
f2 = input("Enter the 2nd favorite fruits: ")
f3 = input("Enter the 3rd favorite fruits: ")

fruits.append(f1)
fruits.append(f2)
fruits.append(f3)

print(fruits)
"""


#Solve :Second way
fruits = []
for i in range(3):
    fruits.append(input("Enter the favorite fruits: "))
   
print(fruits)

"""
#Solve :Third way
fruits = []
fruits.append(input("Enter the 1st favorite fruits: "))
fruits.append(input("Enter the 2nd favorite fruits: "))
fruits.append(input("Enter the 3rd favorite fruits: "))

print(fruits)
"""
