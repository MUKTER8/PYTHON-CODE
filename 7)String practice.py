#Practice with strings
#1. Write a program that asks the user for their name and print it's length.
name = input("What is your name? ")
print("Q:1)The length of your name is", len(name))
#2. Write a program that asks the user for their name and print it in uppercase.
print("Q:2):",name.upper())
#3. Write a program that asks the user for their name and print it in lowercase.
print("Q:3):",name.lower())
#4. Write a program that asks the user for their name and find the occurrence of '$' in string.
print("Q:4):",name.count("$"))  #count() method returns the number of occurrences of a substring in the given string.
#5. Write a program that asks the user for their name and find the occurrence of 'a' in string.
print("Q:5):",name.count("a"))
