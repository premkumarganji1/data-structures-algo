class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        temp = self.head
        while temp is not None:
            if temp.next == self.tail:
                self.tail = temp
                self.tail.next = None
                self.length -= 1
            temp = temp.next

    def prepend(self, value):
        new_node = Node(value)
        temp = self.head
        self.head = new_node
        new_node.next = temp
        self.length += 1

        if self.length == 1:
            self.tail = new_node

    def pop_first(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = None

        self.head = self.head.next
        self.length -= 1
        # self.head = temp

    def get(self, index):
        temp = self.head
        i = 0
        while (i < self.length) and temp is not None:
            if i == index:
                print(f"index: {i}, value: {temp.value}")
                return temp
            i += 1
            temp = temp.next

    def set_value(self, index, value):
        if index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next

        temp.value = value

    def set_value2(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if self.length == 0 or index > self.length:
            return None
        i, temp = 0, self.head
        while i < self.length:
            if i + 1 == index:
                new_node.next = temp.next
                temp.next = new_node

            temp = temp.next
            i += 1

    def insert2(self, index, value):
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()

        temp = self.get(index - 1)
        temp.next = temp.next.next
        self.length -= 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        # after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            # after = after.next


my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
# my_linked_list.pop()
# my_linked_list.prepend(6)
# my_linked_list.pop_first()
# my_linked_list.get(1)
# my_linked_list.set_value(4, 15)
# my_linked_list.insert(1, 20)
# my_linked_list.remove(3)
my_linked_list.reverse()

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
    
"""
