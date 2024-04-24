class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(ll, k):   # my answer
    y = ll.head
    x = ll.head

    if y is None:
        return None
    length = 1
    while y.next is not None:
        y = y.next
        length += 1

    if k > length:
        return None

    for _ in range(length - k):
        x = x.next

    return x


def find_kth_from_end_updated(ll, k):
    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    print(fast.value)

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
#                                             #
#    This is a separate function that is      #
#    not a method within the                  #
#    LinkedList class.                        #
#    INDENT ALL THE WAY TO THE LEFT.          #
#                                             #
###############################################


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

k = 2
# result = find_kth_from_end(my_linked_list, k)
result = find_kth_from_end_updated(my_linked_list, k)

print(result.value)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    7

"""

