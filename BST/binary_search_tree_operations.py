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



"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""

