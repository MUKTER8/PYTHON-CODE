"""You are given a polynomial P of a single indeterminate (or variable),x .
You are also given the values of x and k. Your task is to verify if P(x)=k.

Constraints
All coefficients of polynomial P are integers.
x and y are also integers.

Input Format
The first line contains the space separated values of  and .
The second line contains the polynomial .

Output Format
Print True if P(x)=k. Otherwise, print False.

Sample Input
1 4
x**3 + x**2 + x + 1
Sample Output
True
"""
# Read input
x, k = map(int, input().split())
polynomial = input()

# Evaluate the polynomial at x
result = eval(polynomial, {'x': x})

# Check if the result equals k
print(result == k)
