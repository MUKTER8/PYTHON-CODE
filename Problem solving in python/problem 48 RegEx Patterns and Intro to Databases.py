# RegEx, Patterns, and Intro to Databases
"""
    Output Format

Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.

Sample Input

6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
Sample Output

julia
julia
riya
samantha
tanya
    """
import re

if __name__ == '__main__':
    N = int(input().strip())
    # Initialize an empty list to store names
    names = []
    # Regular expression pattern to match gmail addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    # Loop through each input line
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        # Check if the email matches the gmail pattern
        if re.match(pattern, emailID):
            # If it matches, append the first name to the list
            names.append(firstName)
    # Sort the names alphabetically
    names.sort()
    # Print each name on a new line
    for name in names:
        print(name) 
