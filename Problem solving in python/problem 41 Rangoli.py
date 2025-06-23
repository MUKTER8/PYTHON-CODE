
def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size-1, -1, -1):
        left = alphabet[size-1:i:-1]  # descending part
        center = alphabet[i]          # middle character
        right = alphabet[i+1:size]    # ascending part
        s = '-'.join(left + center + right)
        lines.append(s.center(4 * size - 3, '-'))

    print('\n'.join(lines + lines[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
"""#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------"""

