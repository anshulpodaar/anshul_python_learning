"""
Recursion - Binary Search Tree
"""


class Node:
    def __init__(self, value:int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value:int):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self, value:int) -> bool:
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    # Recursive Contains
    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        return False


    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    # Recursive Insert
    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        # if value == current_node.value:
        #     return None
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


# Recursive Delete
    def __r_delete(self, current_node, value):
        # if current_node is None:
        #     return Node(value)
        # if value < current_node.value:
        #     current_node.left = self.__r_insert(current_node.left, value)
        # if value > current_node.value:
        #     current_node.right = self.__r_insert(current_node.right, value)
        # # if value == current_node.value:
        # #     return None
        # return current_node

    def r_delete(self, value):
        # if self.root is None:
        #     self.root = Node(value)
        # self.__r_insert(self.root, value)

# def _bst_iteratively():
#     print("\n#########################\n")
#
#     my_tree = BinarySearchTree()
#     print(my_tree.root)
#
#     my_tree.insert(2)
#     my_tree.insert(1)
#     my_tree.insert(5)
#     my_tree.insert(3)
#
#     print(my_tree.root.value)
#     print(my_tree.root.left.value)
#     print(my_tree.root.right.value)
#     print(my_tree.root.right.left.value)
#     # print(my_tree.root.right.right.value)
#
#     my_tree = BinarySearchTree()
#     print(my_tree.contains(27))
#     my_tree.insert(47)
#     my_tree.insert(21)
#     my_tree.insert(76)
#     my_tree.insert(18)
#     my_tree.insert(27)
#     my_tree.insert(52)
#     my_tree.insert(82)
#
#     print(my_tree.contains(27))
#     print(my_tree.contains(17))


def _bst_recursively():
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(f"BST contains 27: {my_tree.r_contains(27)}")
    print(f"BST contains 17: {my_tree.r_contains(17)}")




if __name__ == "__main__":
    # _bst_iteratively()
    _bst_recursively()
