class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # self.tail.prev.next = None
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return True

    def get(self, index):

        if index > self.length or index < 0:
            return None

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        return temp

    def get_updated(self, index):

        if index > self.length or index < 0:
            return None

        temp = self.head
        if index < self.length / 2:
            #  for _ in range(index - 1):
            for _ in range(index):     # index from 0
                temp = temp.next

        else:
            temp = self.tail
            #  for _ in range(self.length - index):
            for _ in range(self.length - 1, index, -1):  # index from 0
                temp = temp.prev

        return temp

    def set_value(self, index, value):
        temp = self.get_updated(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length - 1:
            return self.append(value)

        new_node = Node(value)
        temp = self.head

        if index < self.length / 2:
            for _ in range(index - 1):     # index from 0
                temp = temp.next

        else:
            temp = self.tail
            for _ in range(self.length - 1, index - 1, -1):  # index from 0
                temp = temp.prev

        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp
        return temp


my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.append(6)
my_dll.append(7)
my_dll.pop()
my_dll.prepend(15)
my_dll.pop_first()
# my_dll.print_list()
print(f"get value: ", my_dll.get(2).value)
print(f"get value updated: ", my_dll.get_updated(5).value)
my_dll.insert(5, 20)
my_dll.print_list()
