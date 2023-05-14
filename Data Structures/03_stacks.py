"""
Stack
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

    def push(self, value: int):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


print("##################################################")

print("***** Initialize Stack *****")
my_stack = Stack(1)
print(my_stack.top.value)
print()

print("##################################################")

print("***** print_stack method *****")
my_stack.print_stack()
print()

print("##################################################")

print("***** push_stack method *****")
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.print_stack()
print()

print("##################################################")

print("***** pop_stack method *****")
my_stack.print_stack()
print()
print("Pop value: ", my_stack.pop().value)
my_stack.print_stack()
print()
print("Pop value: ", my_stack.pop().value)
my_stack.print_stack()
print()
print("Pop value: ", my_stack.pop().value)
my_stack.print_stack()
print()
print("Pop value: ", my_stack.pop().value)
my_stack.print_stack()
print()
print("Pop value: ", my_stack.pop())
my_stack.print_stack()
print()

print("##################################################")

print("***** push_stack method *****")
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.print_stack()
print()

print("##################################################")
