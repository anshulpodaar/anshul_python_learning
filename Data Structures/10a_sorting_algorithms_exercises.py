"""
Sorting Algorithms
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
"""

import typing

from typing import List, Union, Optional


def bubble_sort(my_list: List) -> List:
    """
    Sorts the list by "bubbling" the largest item to the end, followed by the second largest, and so on.
    :param my_list: List of integers
    :return: my_list: List of integers (sorted)
    """
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def selection_sort(my_list: List) -> List:
    """
    Sorts the list by "selecting" the minimum value that can be assigned to an index one at a time.
    :param my_list: List of integers
    :return: my_list: List of integers (sorted)
    """
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def insertion_sort(my_list: List) -> List:
    """
    Sorts the list by "inserting" the smaller item to the previous spot iteratively.
    :param my_list: List of integers
    :return: my_list: List of integers (sorted)
    """
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while j > -1 and temp < my_list[j]:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

def merge_sort(my_list: List) -> List:
    """
    Sorts the list by
    :param my_list: List of integers
    :return: my_list: List of integers (sorted)
    """
    pass

def quick_sort(my_list: List) -> List:
    """
    Sorts the list by
    :param my_list: List of integers
    :return: my_list: List of integers (sorted)
    """
    pass


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value=Optional):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def bubble_sort(self):
        pass


def _sort():
    my_list = [4, 2, 6, 5, 1, 3]

    #########################
    # Bubble Sort
    print("\n=========================")
    print("BUBBLE SORT")
    # print("-------------------------")

    print(bubble_sort([4, 2, 6, 5, 1, 3]))
    print("=========================")

    #########################
    # Selection Sort
    print("\n=========================")
    print("SELECTION SORT")
    # print("-------------------------")

    print(selection_sort([4, 2, 6, 5, 1, 3]))
    print("=========================")

    #########################
    # Insertion Sort
    print("\n=========================")
    print("INSERION SORT")
    # print("-------------------------")

    print(insertion_sort([4, 2, 6, 5, 1, 3]))
    print("=========================")

    #########################
    # Merge Sort
    print("\n=========================")
    print("MERGE SORT")
    # print("-------------------------")

    print(merge_sort([4, 2, 6, 5, 1, 3]))
    print("=========================")

    #########################
    # Quick Sort
    print("\n=========================")
    print("QUICK SORT")
    # print("-------------------------")

    print(quick_sort([4, 2, 6, 5, 1, 3]))
    print("=========================")

    #########################


if __name__ == "__main__":
    _sort()
