"""
    Given the participants' score sheet for your University Sports Day,
    you are required to find the runner-up score.
    You are given n scores. Store them in a list and find the score of the runner-up.

    """
n = int(input())
score = list(map(int, input().split()))

# Step 1: Find maximum manually
maximum = score[0]
for i in score:
    if i > maximum:
        maximum = i

# Step 2: Initialize second_max as None
second_max = None
for i in score:
    if i != maximum:
        if second_max is None or i > second_max:
            second_max = i

# Step 3: Print result
if second_max is not None:
    print("Second maximum is:", second_max)
else:
    print("Second maximum not found (all numbers same)")
