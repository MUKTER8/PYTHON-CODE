# Function to mutate a string by replacing a character at a given position
def mutate_string(string, position, character):
    # Strings are immutable, so we create a new string with the desired character replaced
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()  # Original string input
    i, c = input().split()  # Position and character to insert
    s_new = mutate_string(s, int(i), c)  # Call the function with converted position
    print(s_new)  # Print the modified string
# Example usage:
# s = "abracadabra" # i = 5
# i = 5, c = "k"
