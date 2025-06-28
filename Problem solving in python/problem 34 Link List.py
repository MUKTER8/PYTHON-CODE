# Problem: Implement a singly linked list with insert and display operations.
# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Linked List Operations


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
# Linked List Insert Operation

    def insert(self, head, data):
        new_node = Node(data)
        if head is None:
            return new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
            return head


# Linked List Implementation
mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)

"""Example usage:
    input:
    5
    1
    2
    3
    4
    5
    output:
    1 2 3 4 5
    """
