n = int(input())
if (n % 2 != 0):
    print("Weird")
elif (n % 2 == 0 & 1 < n < 5):
    print("Not Weird")
elif (n % 2 == 0 & 5 < n < 21):
    print("Weird")
elif (n % 2 == 0 & 20 < n):
    print("Not Weird")
else:
    print("error")

    """
    Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
    """
