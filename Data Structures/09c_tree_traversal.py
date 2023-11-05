"""
Binary Search Tree - Tree traversal
- Breadth-First_Search (BFS)
- Depth-First-Search (DFS)
    - DFS PreOrder
    - DFS PostOrder
    - DFS InOrder
"""

import typing

from typing import List, Union


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
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

    def bfs(self) -> List:
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return results

    def dfs_pre_order(self) -> List:
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self) -> List:
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self) -> List:
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def is_valid_bst(self) -> bool:
        results = self.dfs_in_order()

        for i in range(len(results) - 1):
            if results[i] >= results[i+1]:
                return False
        return True

    def kth_smallest(self, k: int) -> Union[int, None]:
        stack = []
        node = self.root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.value
            node = node.right
        return None


def _tree_traversal():
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    """
    my_tree =           47
                      /    \
                    21      76
                   /  \    /  \
                  18  27  52  82
    """

    #########################
    # Breadth-First-Search (BST)
    print("\n=========================")
    print("Breadth-First-Search (BST)")
    print("-------------------------")

    print(my_tree.bfs()) # [47, 21, 76, 18, 27, 52, 82]
    print("=========================")

    #########################

    # Depth-First-Search PreOrder (DST PreOrder)
    print("\n=========================")
    print("Depth-First-Search PreOrder (DST PreOrder)")
    print("-------------------------")

    print(my_tree.dfs_pre_order()) # [47, 21, 18, 27, 76, 52, 82]
    print("=========================")

    #########################

    # Depth-First-Search PostOrder (DST PostOrder)
    print("\n=========================")
    print("Depth-First-Search PostOrder (DST PostOrder)")
    print("-------------------------")

    print(my_tree.dfs_post_order()) # [18, 27, 21, 52, 82, 76, 47]
    print("=========================")

    #########################

    # Depth-First-Search InOrder (DST InOrder)
    print("\n=========================")
    print("Depth-First-Search InOrder (DST InOrder)")
    print("-------------------------")

    print(my_tree.dfs_in_order()) # [18, 21, 27, 47, 52, 76, 82]
    print("=========================")

    #########################

    # IsValid BST
    print("\n=========================")
    print("IsValid BST")
    print("-------------------------")

    print(my_tree.is_valid_bst()) # True
    print("=========================")

    #########################

    # Kth Smallest Node

    print("\n=========================")
    print("Kth Smallest Node")
    print("-------------------------")

    print(f"1st smallest node: {my_tree.kth_smallest(1)}") # 27
    print(f"2nd smallest node: {my_tree.kth_smallest(2)}")  # 27
    print(f"3rd smallest node: {my_tree.kth_smallest(3)}")  # 27
    print(f"4th smallest node: {my_tree.kth_smallest(4)}")  # 27
    print(f"5th smallest node: {my_tree.kth_smallest(5)}")  # 27
    print(f"6th smallest node: {my_tree.kth_smallest(6)}")  # 27
    print(f"7th smallest node: {my_tree.kth_smallest(7)}")  # 27
    print("=========================")

    #########################


if __name__ == "__main__":
    _tree_traversal()
