"""
Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
E.g:
a=3,b=5
output
8
-2
15
"""
a = int(input())
b = int(input())

sum = a+b
sub = a-b
mul = a*b

print(sum)
print(sub)
print(mul)
