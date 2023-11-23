"""
Quick Sort
"""

import typing
from typing import List


def swap(my_list: List, index1: int, index2: int) -> None:
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    # return None


def pivot(my_list: List, pivot_index: int, end_index: int) -> int:
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list: List, left: int, right: int) -> List:
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list


def quick_sort(my_list: List) -> List:
    return quick_sort_helper(my_list, 0, len(my_list)-1)


def _quick_sort():
    #########################
    # Pivot Helper Function
    print("\n=========================")
    print("PIVOT HELPER FUNCTION")
    # print("-------------------------")

    my_list = [4, 6, 1, 7, 3, 2, 5]
    print("original List: ", my_list)
    pivot_index = pivot(my_list, 0, 6)
    print("Pivot index: ", pivot_index)
    print("Pivoted List: ", my_list)

    #########################
    #########################
    # Quick Sort
    print("\n=========================")
    print("QUICK SORT")
    # print("-------------------------")

    my_list = [1, 2, 7, 8, 3, 4, 5, 6]
    print("original List: ", my_list)
    my_list = quick_sort(my_list)
    print("Sorted List: ", my_list)

    print()

    my_list = [4, 6, 1, 7, 3, 2, 5]
    print("original List: ", my_list)
    my_list = quick_sort(my_list)
    print("Sorted List: ", my_list)

    print()

    my_list = [3, 2, 1]
    print("original List: ", my_list)
    my_list = quick_sort(my_list)
    print("Sorted List: ", my_list)

    print("=========================")
    #########################


if __name__ == "__main__":
    _quick_sort()
