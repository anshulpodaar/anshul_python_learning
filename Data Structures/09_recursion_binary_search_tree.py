"""
Recursion - Binary Search Tree
"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
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

    def contains(self, value: int) -> bool:
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
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        if value == current_node.value:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete(current_node.right, sub_tree_min)
        return current_node

    def r_delete(self, value):
        self.__r_delete(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


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
    #########################
    # Recursive Contains
    print("\n=========================")
    print("RECURSIVE CONTAINS")
    print("-------------------------")
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(f"BST contains 27: {my_tree.r_contains(27)}")  # True
    print(f"BST contains 17: {my_tree.r_contains(17)}")  # False
    print("=========================")

    #########################
    # Recursive Insert
    print("\n=========================")
    print("RECURSIVE INSERT")
    print("-------------------------")
    my_tree = BinarySearchTree()
    my_tree.r_insert(2)
    my_tree.r_insert(1)
    my_tree.r_insert(3)

    """
    The lines create this tree:
         2
        / \
       1   3
    """

    print("Root: ", my_tree.root.value)  # 2
    print("Root -> Left: ", my_tree.root.left.value)  # 1
    print("Root -> Right: ", my_tree.root.right.value)  # 3
    print("=========================")

    #########################
    # Minimum Value
    print("\n=========================")
    print("MINIMUM VALUE")
    print("-------------------------")
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print("Min value in entire tree: ", my_tree.min_value(my_tree.root))  # 18
    print("Min value in right sub-tree: ", my_tree.min_value(my_tree.root.right))  # 52
    print("=========================")

    #########################
    # Recursive Insert
    print("\n=========================")
    print("RECURSIVE DELETE")
    print("-------------------------")
    my_tree = BinarySearchTree()
    my_tree.r_insert(2)
    my_tree.r_insert(1)
    my_tree.r_insert(3)

    """
    The lines create this tree:
         2
        / \
       1   3
    """

    print("root =", my_tree.root.value)  # 2
    print("root.left =", my_tree.root.left.value)  # 1
    print("root.right =", my_tree.root.right.value)  # 3

    my_tree.r_delete(2)

    """
    The 2 node is deleted and the 3 node is moved up
         3
        / \
       1   None
    """
    print("\nroot =", my_tree.root.value)  # 3
    print("root.left =", my_tree.root.left.value)  # 1
    print("root.right =", my_tree.root.right)  # None
    print("=========================")

    #########################


if __name__ == "__main__":
    # _bst_iteratively()
    _bst_recursively()
