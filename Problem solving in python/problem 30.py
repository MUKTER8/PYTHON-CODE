# Problem 30: Text Warping
# Task: Use string methods to format the output of a warped text structure.
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string = input("Enter the string to be wrapped: ")
    max_width = int(input("Enter the maximum width for wrapping: "))
    wrapped_text = wrap(string, max_width)
    print(wrapped_text)