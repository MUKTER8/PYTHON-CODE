X = []
W = []

n = int(input("Enter the number of elements: "))

# Take all values in a single line
X = list(map(int, input("Enter values (space-separated): ").split()))

# Take all weights in a single line
W = list(map(int, input("Enter weights (space-separated): ").split()))

# Function to calculate weighted mean
def WeightedMean(X, W):
    total_weighted_sum = 0
    total_weight = 0
    for i in range(n):
        total_weighted_sum += X[i] * W[i]
        total_weight += W[i]
    return total_weighted_sum / total_weight

# Calling the function and printing the result
result = WeightedMean(X, W)
print("Weighted Mean:", round(result, 1))
