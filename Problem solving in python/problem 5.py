"""The included code stub will read an integer,n, from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.

Example
n=5
Print the string 12345."""
n = int(input())
i = 1
while (i <= n):
    print(i, end="")
    i = i+1
