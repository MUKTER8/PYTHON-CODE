# Check prime number or not
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


for n in num:
    if is_prime(n):
        print(f"{n} prime")
    else:
        print(f"{n} not prime")

    """
Sample Input
3
12
5
7
Sample Output
12 Not prime
5 Prime
7 Prime
    """
