"""
Linked List Constructor definition
"""

import typing
from typing import Optional


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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

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

    def prepend(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_2(self):
        if self.head is None:
            return None
        elif self.length == 1:
            temp = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.tail
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            self.tail = prev
            self.tail.next = None
            self.length -= 1
        return temp

    def pop(self):
        if self.length == 0:
            return None
        prev = self.head
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index not in range(self.length):
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index not in range(self.length + 1):
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = ListNode(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        if self.length <= 1:
            return False
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    def find_middle_node(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def has_loop(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False




print("##################################################")

print("***** Initialize LinkedList *****")
my_linked_list = LinkedList(1)
print(my_linked_list.head.value)
print()

print("##################################################")

print("***** print_list method *****")
my_linked_list.print_list()
print()

print("##################################################")

print("***** append method *****")
my_linked_list.append(2)
my_linked_list.print_list()
print()

my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
print()

print("##################################################")

print("***** pop method *****")
print(my_linked_list.pop())
my_linked_list.print_list()
print()

print(my_linked_list.pop())
my_linked_list.print_list()
print()

print(my_linked_list.pop())
my_linked_list.print_list()
print()

print(my_linked_list.pop())
my_linked_list.print_list()
print()

print(my_linked_list.pop())
my_linked_list.print_list()
print()

print("##################################################")

print("***** prepend method *****")
my_linked_list.prepend(1)
my_linked_list.print_list()
print()

my_linked_list.prepend(2)
my_linked_list.print_list()
print()

my_linked_list.prepend(3)
my_linked_list.print_list()
print()

print("##################################################")

print("***** pop_first method *****")
print(my_linked_list.pop_first())
my_linked_list.print_list()
print()

print(my_linked_list.pop_first())
my_linked_list.print_list()
print()

print(my_linked_list.pop_first())
my_linked_list.print_list()
print()

print(my_linked_list.pop_first())
my_linked_list.print_list()
print()

print("##################################################")

my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print("***** get method *****")
print(my_linked_list.get(2))
# my_linked_list.print_list()
print()

print("##################################################")

print("***** set_value method *****")
print(my_linked_list.set_value(1, 5))
my_linked_list.print_list()
print()

print("##################################################")

print("***** insert method *****")
print(my_linked_list.insert(2, 6))
my_linked_list.print_list()
print()

print("##################################################")

print("***** remove method *****")
print(my_linked_list.remove(2))
my_linked_list.print_list()
print()

print("##################################################")

print("***** reverse method *****")
print(my_linked_list.reverse())
my_linked_list.print_list()
print()

print("##################################################")

print("***** find_middle_node method *****")
my_linked_list.print_list()
print("Middle Node:", my_linked_list.find_middle_node().value)
print()
my_linked_list.append(6)
my_linked_list.print_list()
print("Middle Node:", my_linked_list.find_middle_node().value)
print()

print("##################################################")

print("***** middleNode method *****")
ll1 = LinkedList()
print("Middle Node:", ll1.middleNode(head = [1,2,3,4,5]).value)
print("Middle Node:", ll1.middleNode(head=[1,2,3,4,5,6]).value)
print()

print("##################################################")
