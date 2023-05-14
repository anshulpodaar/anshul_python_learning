"""
Stacks Constructor definition
"""

import typing
from typing import Optional


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, value=Optional):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next



print("##################################################")

print("***** Initialize Stack *****")
my_stack = Stack(4)
print(my_stack.top.value)
print()

print("##################################################")

print("***** print_stack method *****")
my_stack.print_stack()
print()

print("##################################################")
