# Definition for singly-linked list.
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Solution:
    def reverseList(self, head):
        current = head
        before = None

        while current:
            temp = current.next
            current.next = before

            before = current
            current = temp

        return before

    def loop_length(self, head):
        if head is None or head.data is None:
            return None

        length = 1
        while head.next:
            length +=1
            head = head.next

        return length

def reverseList_recursion(head):

    # returns only base case
    if head is None or head.next is None:
        return head

    new_node = reverseList_recursion(head.next)
    front = head.next
    front.next = head
    head.next = None

    return new_node


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverseList_recursion(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)

print(Solution.loop_length(None, head))