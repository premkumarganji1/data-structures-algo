class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if value == temp.value:
                return False

            elif value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True

                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True

                temp = temp.left

    def contains(self, value):
        if self.root is None:
            return False

        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True

            elif value > temp.value:
                temp = temp.right

            else:
                temp = temp.left

        return False

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        elif value == current_node.value:
            return True
        elif value < current_node.value:
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert_old(self, current_node, value):
        if current_node is None:
            self.root = Node(value)
            return current_node

        elif current_node.value < value:
            if current_node.right is None:
                current_node.right = Node(value)
                return
            self.__r_insert(current_node.right, value)
        else:
            if current_node.left is None:
                current_node.left = Node(value)
                return
            self.__r_insert(current_node.left, value)

    def r_insert_old(self, value):
        self.__r_insert(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)

        elif current_node.value < value:
            current_node.right = self.__r_insert(current_node.right, value)
        else:
            current_node.left = self.__r_insert(current_node.left, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def find_min(self, current_node):
        while current_node.left is None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        elif current_node.value < value:
            return self.__delete_node(current_node.right, value)
        elif current_node.value > value:
            return self.__delete_node(current_node.left, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min_val = self.find_min(current_node.right)
                current_node.value = sub_tree_min_val
                current_node = self.__delete_node(current_node.right, sub_tree_min_val)

        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)





# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(25)
# my_tree.insert(29)
# my_tree.insert(26)
# my_tree.insert(28)
# my_tree.insert(30)
# my_tree.insert(76)
# my_tree.insert(52)
# my_tree.insert(82)

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)
print('Root->Left:', my_tree.root.left.value)
print('Root->Right:', my_tree.root.right.value)
print('contains: ', my_tree.contains(3))
print('contains: ', my_tree.contains(5))
print('r contains: ', my_tree.r_contains(3))
print('r contains: ', my_tree.r_contains(5))
my_tree.r_insert(4)
print('Root->Right:', my_tree.root.right.right.value)
print('r contains: ', my_tree.r_contains(4))

"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""

