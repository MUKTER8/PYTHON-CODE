"""
    Sample Input
ABCDCDC
CDC
Sample Output
2
    """


def count_substring(string, sub_string):
    count = 0
    start = 0
    while True:
        pos = string.find(sub_string, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1  # move one step forward to allow overlapping
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
# This program counts the number of occurrences of a substring in a string.
# It takes two inputs: the main string and the substring to search for.
