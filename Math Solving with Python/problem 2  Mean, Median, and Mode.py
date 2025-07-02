# Mean, Median, and Mode Calculation
def Mean(numbers):
    return sum(numbers) / len(numbers)


def Median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]


def Mode(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]
    return min(modes)  # Return the smallest mode if multiple


def main():
    n = int(input("Enter the number of elements: "))
    numbers = list(
        map(int, input("Enter the numbers separated by spaces: ").split()))

    print("Mean:", Mean(numbers))
    print("Median:", Median(numbers))
    print("Mode:", Mode(numbers))


main()
