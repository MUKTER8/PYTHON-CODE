"""Input Format

A single line containing a S string .

Constraints


Output Format

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
    """
if __name__ == '__main__':
    s = input()  # Read the input string

    # Check for alphanumeric characters
    print(any(c.isalnum() for c in s))
    # Check for alphabetical characters
    print(any(c.isalpha() for c in s))
    # Check for digits
    print(any(c.isdigit() for c in s))
    # Check for lowercase characters
    print(any(c.islower() for c in s))
    # Check for uppercase characters
    print(any(c.isupper() for c in s))
# The code checks various properties of the input string and prints True or False accordingly.