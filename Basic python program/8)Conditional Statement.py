#Learn Conditional Statement in Python, if, else, elif, nested if, if-elif-else
"""Write a program that asks the user for their name and print it's length. If the length is greater than 10,
print "Your name is too long." otherwise print "Your name is short."""
name=input("What is your name? ")
if len(name)>10:
    print("Your name is too long.")
else:
    print("Your name is short.")
"""Write a program that asks the user for their marks and print their grade according to the following criteria:
100>=90,Grade=A+, 89>=80,Grade=A, 79>=70,Grade=B, 69>=60,Grade=C, 59>=50,Grade=D, 49>=40,Grade=E, 39>=0,Grade=F."""
marks=float(input("What is your marks? ")) #marks is an integer
if marks>=90:
    print("Grade=A+") #Grade=A+
elif marks>=80:
    print("Grade=A") #Grade=A
elif marks>=70:
    print("Grade=A-") #Grade=A-
elif marks>=60:
    print("Grade=B") #Grade=B
elif marks>=50:
    print("Grade=C") #Grade=C
elif marks>=40:
    print("Grade=E") #Grade=E
else:
    print("Grade=F") #Grade=F
    
    
#Write a program that asks the user for their age and print "You are a child." if the age is less than 18, "You are a teenager." if the age is less than 13, "You are an adult." otherwise.
age=int(input("What is your age? ")) #age is an integer
if age<13:
    print("You are a teenager.")
elif age<18:
    print("You are a child.")
else:
    print("You are an adult.")
# Write a program for check number is even or odd
num=int(input("Enter a number: ")) #num is an integer
if num%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
# Write a program for check number is positive or negative
num=int(input("Enter a number: ")) #num is an integer
if num>0:
    print("The number is positive.")
elif num<0:
    print("The number is negative.")
else:
    print("The number is zero.")
# Write a program for check number is greater than 100 or not
num=int(input("Enter a number: ")) #num is an integer
if num>100:
    print("The number is greater than 100.")
else:
    print("The number is not greater than 100.")

#Write a program to find the largest number among three numbers.
num1=int(input("Enter first number: ")) #num1 is an integer
num2=int(input("Enter second number: ")) #num2 is an integer
num3=int(input("Enter third number: ")) #num3 is an integer 
if num1>num2 and num1>num3:
    print(num1,"is the largest number.")    
elif num2>num1 and num2>num3:
    print(num2,"is the largest number.")
else:
    print(num3,"is the largest number.")
    
