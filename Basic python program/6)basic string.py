#Basics string
#String is a sequence of characters
#String is a immutable data type
#String can be enclosed in single quotes or double quotes
#String can be enclosed in triple single quotes or triple double quotes
#String can be enclosed in single quotes or double quotes
str1="This is a string.\nWe are learning python."
str2='this is also a string.'
str3='''Learning python is fun!'''
print(str1)
# using concatenation operator for joining two strings
#Syntax: string1+string2
str4=str2+" "+str3
print(str4)
#using length operator for finding the length of a string
#Syntax: len(string_name)
print(len(str4))

#indexing is used to access individual characters in a string
#Indexing starts from 0
#Negative indexing is also possible
#Negative indexing starts from -1
#Does't manipulate the original string
print(str4[0])
print(str4[-10])

#Slicing is used to access a range of characters in a string
#Syntax: string_name[starting_index:ending_index+1]
#starting_index is inclusive but ending_index is exclusive
print(str1[0:5])
print(str1[5:]) #if ending index is not given, it will go till the end of the string
print(str1[:5]) #if starting index is not given, it will start from the beginning of the string
print(str1[:]) #if starting index and ending index are not given, it will print the whole string
print(str1[0:5:2]) #step size is 2 it's means it will print 0,2,4 index character of string
print(str1[::-1]) #reverse the string ,tep size is -1 it's means it will print string in reverse order
print(str1[5:0:-1]) #reverse the string from 5 to 1 index
print(str1[5::-1]) #reverse the string from 5 to 0 index
print(str1[:5:-1]) #reverse the string from 5 to end of the string

#String functions and methods in python, syntax: string_name.function_name() or string_name.method_name() or function_name(string_name) or method_name(string_name) 
#1. capitalize() - It will capitalize the first character of the string
print(str2.capitalize()) #Tis function will capitalize the first character of the string it's means it will make first character of the string in capital letter
#2. casefold() - It will convert the string into lowercase
print(str2.casefold()) #This function will convert the string into lowercase           
#3. center() - It will center align the string
print(str2.center(50)) #This function will center align the string
#4. count() - It will count the number of occurrences of a substring in the string
print(str2.count('i')) #This function will count the number of occurrences of a substring in the string
#5. encode() - It will encode the string
print(str2.encode()) #This function will encode the string
#6. endswith() - It will check if the string ends with a particular substring
print(str2.endswith('g.')) #This function will check if the string ends with a particular substring
#7. expandtabs() - It will expand the tabs in the string
str5="Hello\tWorld"
print(str5.expandtabs(2)) #This function will expand the tabs in the string
#8. find() - It will find the first occurrence of a substring in the string
print(str2.find('i')) #This function will find the first occurrence of a substring in the string
#9. format() - It will format the string
str6="Hello, my name is {}"
print(str6.format('John')) #This function will format the string
#10. Replace() - It will replace a substring with another substring
print(str2.replace('is','e')) #This function will replace a substring with another substring
#11. split() - It will split the string into a list of strings
print(str2.split()) #This function will split the string into a list of strings
#12. strip() - It will remove the leading and trailing whitespaces from the string
str7="   Hello, World   "
print(str7.strip()) #This function will remove the leading and trailing whitespaces from the string
#13. swapcase() - It will swap the cases of the characters in the string
str8="Hello, World"
print(str8.swapcase()) #This function will swap the cases of the characters in the string