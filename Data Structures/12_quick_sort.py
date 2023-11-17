"""
Quick Sort
"""

import typing
from typing import List


def merge_sorted_lists(list1: List, list2: List) -> List:
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def quick_sort(my_list: List) -> List:
    pass


def _quick_sort():
    #########################
    # Merge Helper Function
    print("\n=========================")
    print("Merge Helper Function")
    # print("-------------------------")

    print(merge_sorted_lists([1, 2, 7, 8], [3, 4, 5, 6]))
    print(merge_sorted_lists([1, 2, 5, 6], [3, 4, 7, 8]))
    print("=========================")

    #########################
    #########################
    # Merge Sort
    print("\n=========================")
    print("MERGE SORT")
    # print("-------------------------")

    original_list = [1, 2, 7, 8, 3, 4, 5, 6]
    sorted_list = quick_sort(original_list)
    print("original List: ", original_list)
    print("Sorted list: ", sorted_list)

    print()

    original_list = [4, 6, 1, 7, 3, 2, 5]
    sorted_list = quick_sort(original_list)
    print("original List: ", original_list)
    print("Sorted list: ", sorted_list)

    print()


original_list = [3, 2, 1]
    sorted_list = quick_sort(original_list)
    print("original List: ", original_list)
    print("Sorted list: ", sorted_list)
    print("=========================")
    #########################


if __name__ == "__main__":
    _merge_sort()
