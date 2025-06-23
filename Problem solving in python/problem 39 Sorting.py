"""
Sorting:
Sample Input 1
3
3 2 1
Sample Output 1
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
    """

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    swaps = 0
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
    print("Sorted Array: {}".format(a))
