def new_func():
    n = int(input())
    tup = tuple(map(int, input().split()))
    print(abs(hash(tup)))


new_func()
