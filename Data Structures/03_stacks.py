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
print("##################################################")
print("##################################################")


class Stack_using_List:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        else:
            temp = self.stack_list.pop()
            return temp




print("##################################################")
print()

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop())

print("\nStack after pop():")
my_stack.print_stack()

print("##################################################")

def is_balanced_parentheses(s: str) -> bool:
    parentheses_map = {")": "(", "}": "{", "]": "["}
    check_list = Stack_using_List()
    for item in s:
        if item in parentheses_map.values():
            check_list.push(item)
        elif item in parentheses_map.keys():
            if check_list.is_empty() or check_list.pop() != parentheses_map[item]:
                return False
    if check_list.is_empty():
        return True
    else:
        return False


###############################################


balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'

print(is_balanced_parentheses(balanced_parentheses))
print(is_balanced_parentheses(unbalanced_parentheses))

###############################################

def reverse_string(s:str) -> str:
    my_stack = Stack_using_List()
    for letter in s:
        my_stack.push(letter)
    new_str = ""
    while not my_stack.is_empty():
        new_str = new_str + my_stack.pop()
    return new_str

my_string = 'hello'
print (reverse_string(my_string))

###############################################

def sort_stack(unsorted_stack:Stack)->Stack:
    sorted_stack = Stack_using_List()
    while not unsorted_stack.is_empty():
        temp = unsorted_stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            temp2 = sorted_stack.pop()
            unsorted_stack.push(temp2)
        sorted_stack.push(temp)
    while not sorted_stack.is_empty():
        temp = sorted_stack.pop()
        unsorted_stack.push(temp)
    return unsorted_stack

###############################################

my_stack = Stack_using_List()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()

###############################################