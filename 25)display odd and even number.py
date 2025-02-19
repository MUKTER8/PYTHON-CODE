n = int(input("Enter the value of n for odd and even : "))
i = 1
print("Display odd number :")
while i <= n:
    if (i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1
    
i=1
print("Display even number :")
while i <= n:
    if (i % 2 != 0):
        i += 1
        continue
    print(i)

    i+= 1
