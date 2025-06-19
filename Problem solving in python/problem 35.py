# Exceptions - String to Integer
try:
    S = input()
    num = int(S)
    print(num)
except ValueError:
    print("Bad String")
