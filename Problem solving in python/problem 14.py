"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position .
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command 
will be of the 7 types listed above. Iterate through each command in order and perform the 
corresponding operation on your list.
"""
List = []
i = 0

def process_command(command):
    parts = command.strip().split()
    if parts[0] == "append":
        List.append(int(parts[1]))
    elif parts[0] == "insert":
        List.insert(int(parts[1]), int(parts[2]))
    elif parts[0] == "print":
        print(List)
    elif parts[0] == "remove":
        List.remove(int(parts[1]))
    elif parts[0] == "pop":
        List.pop()
    elif parts[0] == "sort":
        List.sort()
    elif parts[0] == "reverse":
        List.reverse()

if __name__ == '__main__':
    N = int(input())
    while (i < N):
        lang = input()
        process_command(lang)
        i=i+1


