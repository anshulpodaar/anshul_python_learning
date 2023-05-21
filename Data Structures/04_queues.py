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
print("##################################################")
print("##################################################")

class Queue_using_List:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # WRITE ENQUEUE MEHTOD HERE #
    def enqueue(self, value: int):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return self

    def dequeue(self):
        if len(self.stack1) > 0:
            return self.stack1.pop()
        else:
            return None

    #############################

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0


# Create a new queue
q = Queue_using_List()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())

# Output the front of the queue
print("Front of the queue:", q.peek())

# Dequeue some values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

# Enqueue another value
q.enqueue(4)

# Output the front of the queue again
print("Front of the queue:", q.peek())

# Dequeue all remaining values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())

# Dequeue from an empty queue and check if it returns None
print("Dequeued value from empty queue:", q.dequeue())

