"""Given an array,A, of N integers, print A's 
elements in reverse order as a 
single line of space-separated numbers.
input:
4
1 2 3 4
output:
4 3 2 1
"""
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
print(*arr)