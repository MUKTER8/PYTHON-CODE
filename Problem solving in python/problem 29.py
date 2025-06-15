# Problem 29: Text Alignment
# Task: Use string methods to format the output of a pyramid-like structure.
#Replace all ______ with rjust, ljust or center. 

thickness = int(input())  # Must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * (2 * i + 1)).center(thickness * 2))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
