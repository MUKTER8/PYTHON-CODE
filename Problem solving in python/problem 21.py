"""Given a base-10 integer,n, convert it to binary (base-2). Then find and print 
    the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. 
    When working with different bases, it is common to show the base as a subscript.
    n=125
    The binary representation of 125 is 1111101. 
    In base 10, there are 5 and 1 consecutive ones in two groups. 
    Print the maximum, 5.
    """
n = int(input("Enter a decimal number: "))
binary = bin(n)[2:]

max_count = 0
current_count = 0

for bit in binary:
    if bit == '1':
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print("Binary:", binary)
print("Max consecutive 1s:", max_count)
