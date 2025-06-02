"""
    x=1
    y=1
    z=2,
    n=3
    all permutations of [i,j,k] are:
    [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[0,1,2],[1,0,2],[1,0,1],[1,1,0],[1,1,1],[1,1,2]]
   print an array of the element that do not sum to n=3
    [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,2]]

    """
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                result.append([i, j, k])
print(result)
