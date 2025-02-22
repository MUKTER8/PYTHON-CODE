# Recursive function
def show(n):
    if (n == 0):
        return
    print(n, end=" ")
    show(n-1)


show(5)
