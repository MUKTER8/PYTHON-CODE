def new_func():
    n = int(input())
    tup = tuple(map(int, input().split()))
    print(hash(tup))


new_func()
"""Print the result of hash(t).
    """
