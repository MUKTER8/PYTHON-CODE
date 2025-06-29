
MOD = 1000000007

n = int(input())
arr = [int(input()) for _ in range(n)]

for num in arr:
    Sn = (num % MOD) * (num % MOD) % MOD  # Sn = n^2 % MOD
    print(Sn)

"""
# Tn = (n * n) - ((n - 1) * (n - 1))
# Sn = T1 + T2 + T3 + ... + Tn
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
S = []
for el in arr:
    Sn = 0
    for j in range(1, el + 1):
        Tn = (j * j) - ((j - 1) * (j - 1))  # বা Tn = 2 * j - 1
        Sn += Tn
    S.append(Sn)
for val in S:
    print(val)

"""
"""
Tn=(n*n)-((n-1)*(n-1))
Sn=T1+T2+T3+...+Tn
input:
n=2
2;where T1=1,T2=2
1;where T1=1
output:
4;where Sn=4
1;where S1=1
"""
