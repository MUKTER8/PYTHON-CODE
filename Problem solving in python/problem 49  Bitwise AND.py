import math
import os
import random
import re
import sys


def bitwiseAnd(N, K):
    if ((K - 1) | K) <= N:
        return K - 1
    else:
        return K - 2


if __name__ == '__main__':
    fptr = open('output49.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()

    """
# Problem 49: Bitwise AND
Explanation:
This code defines a function `bitwiseAnd` that calculates the maximum value of `A & B` for all pairs `(A, B)` such that `1 <= A < B <= N` and `B < K`.
The function checks if the bitwise OR of `K - 1` and `K` is less than or equal to `N`. If it is, it returns `K - 1`, otherwise it returns `K - 2`. The main part of the code reads multiple test cases, processes each case, and writes the results to an output file.
Sample Input

STDIN   Function
-----   --------
3       T = 3
5 2     N = 5, K = 2
8 5     N = 8, K = 5
2 2     N = 2, K = 2
Sample Output

1
4
0
    """
