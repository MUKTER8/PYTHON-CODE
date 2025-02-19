list = (1, 2, 3, 4, 6, 3, 6, 3, 7, 9, 3, 9, 34, 8, 9, 45)
x = int(input("Which number you find :"))
i = 0
while i < len(list):
    if (list[i] == x):
        print("found at index:",i)
        break
    else:
        print("not found")
    i = i + 1
 
