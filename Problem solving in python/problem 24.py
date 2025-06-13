arr = []
for _ in range(6):
    arr.append(list(map(int, input().split())))

max_sum = -63  # minimum possible value (-9 * 7)
for i in range(4):
    for j in range(4):
        hourglass = (
            arr[i][j] + arr[i][j+1] + arr[i][j+2]
            + arr[i+1][j+1]
            + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        )
        max_sum = max(max_sum, hourglass)

print(max_sum)
"""
This program finds the maximum hourglass sum in a 6x6 2D array.
input:
1 1 1 1 0 0
0 1 0 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 4
0 0 0 2 4 4
output:
21
"""
