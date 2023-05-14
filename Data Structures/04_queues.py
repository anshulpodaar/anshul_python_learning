"""
Queue
"""

import typing
from typing import Optional


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self, value=Optional):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value: int):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


print("##################################################")

print("***** Initialize Queue *****")
my_queue = Queue(1)
print(my_queue.first.value)
print()

print("##################################################")

print("***** print_queue method *****")
my_queue.print_queue()
print()

print("##################################################")

print("***** enqueue method *****")
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.print_queue()
print()

print("##################################################")

print("***** dequeue method *****")
my_queue.print_queue()
print()
print("Dequeue value: ", my_queue.dequeue().value)
my_queue.print_queue()
print()
print("Dequeue value: ", my_queue.dequeue().value)
my_queue.print_queue()
print()
print("Dequeue value: ", my_queue.dequeue().value)
my_queue.print_queue()
print()
print("Dequeue value: ", my_queue.dequeue().value)
my_queue.print_queue()
print()
print("Dequeue value: ", my_queue.dequeue())
my_queue.print_queue()
print()

print("##################################################")

print("***** enqueue method *****")
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.print_queue()
print()

print("##################################################")
