"""Given a string,S, of length N that is indexed from 0 toN-1, print its even-indexed and odd-indexed 
    characters as 2 space-separated strings on a single line (see the Sample below for more detail).
    input:abcdef
    output:abc def
    """
n=int(input())
for _ in range(n):
    S  = str(input())
    even_indexed = S[::2]
    odd_indexed = S[1::2]
    print(even_indexed, odd_indexed)
