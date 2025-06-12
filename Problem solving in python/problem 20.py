"""The first line contains an integer,n, denoting the number of entries in the phone book.
Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line. 
The first value is a friend's name, and the second value is an 8-digit phone number.
After the  lines of phone book entries, there are an unknown number of lines of queries. 
Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.
"""
# Read number of entries
n = int(input())

# Create an empty dictionary
phone_book = {}

# Input names and numbers
for _ in range(n):
    entry = input().split()
    name = entry[0]
    number = entry[1]
    phone_book[name] = number

# Now take queries until EOF (End Of File)
try:
    while True:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
except EOFError:
    pass
