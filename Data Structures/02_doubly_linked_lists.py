"""
Doubly Linked List
"""

import typing
from typing import Optional


class ListNode:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
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

    # def make_empty(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index not in range(self.length):
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
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
        before = self.get(index-1)
        after = before.next
        new_node.next = after
        new_node.prev = before
        after.prev = new_node
        before.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        before = self.get(index-1)
        temp = before.next
        after = temp.next
        temp.prev = None
        temp.next = None
        before.next = after
        after.prev = before
        self.length -= 1
        return temp

    # def reverse(self):
    #     if self.length == 0:
    #         return False
    #     elif self.length == 1:
    #         return True
    #     temp = self.head
    #     self.head = self.tail
    #     self.tail = temp
    #     after = temp.next
    #     before = None
    #     for _ in range(self.length):
    #         after = temp.next
    #         temp.next = before
    #         before = temp
    #         temp = after
    #     return True

    # def find_middle_node(self):
    #     if self.head is None:
    #         return None
    #     slow = self.head
    #     fast = self.head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #     return slow
    #
    # # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # #     if head is None:
    # #         return None
    # #     slow = fast = head
    # #     while fast and fast.next:
    # #         fast = fast.next.next
    # #         slow = slow.next
    # #     return slow
    #
    # def has_loop(self):
    #     if self.head is None:
    #         return False
    #     slow = self.head
    #     fast = self.head
    #     while fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #         if fast == slow:
    #             return True
    #     return False
    #
    # def find_kth_from_end(self, k:int):
    #     slow = self.head
    #     fast = self.head
    #     i = 0
    #     while i < k:
    #         if fast is None:
    #             return None
    #         if fast==self.tail:
    #             fast = None
    #         else:
    #             fast = fast.next
    #         i += 1
    #     while fast is not None:
    #         fast = fast.next
    #         slow = slow.next
    #     return slow
    #
    # def reverse_between(self, m, n):
    #     if self.length < 2:
    #         return None
    #     if m >= self.length or n >= self.length or m > n:
    #         return None
    #     dummy = ListNode(0)
    #     dummy.next = self.head
    #     self.head = dummy
    #     prev = self.head
    #     for i in range(0, m):
    #         prev = prev.next
    #     curr = prev.next
    #     for i in range(0, n-m):
    #         temp = curr.next
    #         curr.next = temp.next
    #         temp.next = prev.next
    #         prev.next = temp
    #         self.tail = curr
    #     self.head = dummy.next
    #     return True
    #
    # def reverseList(self):
    #     if not self.head.next:
    #         return None
    #     prev = self.head
    #     curr = self.head.next
    #     temp = self.head.next.next
    #     self.tail = self.head
    #     self.tail.next = None
    #     while temp:
    #         curr.next = prev
    #         prev = curr
    #         curr = temp
    #         temp = temp.next
    #     curr.next = prev
    #     self.head = curr
    #     return self.head
    #
    # def partition_list(self, x):
    #     if not self.head:
    #         return None
    #     temp = self.head
    #     ll1 = None
    #     ll2 = None
    #     while temp:
    #         if temp.value < x:
    #             if not ll1:
    #                 ll1 = DoublyLinkedList(temp.value)
    #             else:
    #                 ll1.append(temp.value)
    #         else:
    #             if not ll2:
    #                 ll2 = DoublyLinkedList(temp.value)
    #             else:
    #                 ll2.append(temp.value)
    #         temp = temp.next
    #     if ll2:
    #         temp = ll2.head
    #     while temp:
    #         ll1.append(temp.value)
    #         temp = temp.next
    #     return ll1
    #
    # def remove_duplicates(self):
    #     curr = self.head
    #     while curr:
    #         temp = curr
    #         while temp:
    #             if temp.next and temp.next.value == curr.value:
    #                 temp.next = temp.next.next
    #                 self.length -= 1
    #             else:
    #                 temp = temp.next
    #         curr = curr.next
    #     return True

    def swap_first_last(self):
        if self.length == 0:
            return False
        elif self.length == 1:
            return True
        else:
            temp = self.head.value
            self.head.value = self.tail.value
            self.tail.value = temp
        return True

    def is_palindrome(self):
        if self.length <= 1:
            return True
        else:
            forward = self.head
            reverse = self.tail
            for _ in range(int(self.length/2) + 1):
                if forward.value != reverse.value:
                    return False
                forward = forward.next
                reverse = reverse.prev
        return True

    def swap_pairs2(self):
        if self.length <= 1:
            return False
        else:
            before = self.head
            after = self.head.next

            while after:
                temp = before.prev
                before.prev = after
                before.next = after.next
                if before.next:
                    before.next.prev = before
                after.prev = temp
                after.next = before
                before = before.next
                after = before.next

            self.head = self.head.prev
            self.tail = self.tail.next
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return False
        else:
            dummy_node = ListNode()
            dummy_node.next = self.head
            before = dummy_node
            self.head = dummy_node
            while before.next and before.next.next:
                one = before.next
                two = before.next.next
                before.next = two
                one.next = two.next
                two.next = one
                two.prev = before
                one.prev = two
                if one.next:
                    one.next.prev = one
                before = before.next.next
            self.head = dummy_node.next
            self.head.prev = None
            dummy_node.next = None
            if self.tail.next:
                self.tail = self.tail.next
            return True





print("##################################################")

print("***** Initialize LinkedList *****")
my_linked_list = DoublyLinkedList(1)
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
my_linked_list.print_list()
print()
print(my_linked_list.get(1))
print(my_linked_list.get(2))
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

# print("***** reverse method *****")
# print(my_linked_list.reverse())
# my_linked_list.print_list()
# print()
#
# print("##################################################")

# print("***** find_middle_node method *****")
# my_linked_list.print_list()
# print("Middle Node:", my_linked_list.find_middle_node().value)
# print()
# my_linked_list.append(6)
# my_linked_list.print_list()
# print("Middle Node:", my_linked_list.find_middle_node().value)
# print()
#
# print("##################################################")
#
# # print("***** middleNode method *****")
# # ll1 = LinkedList()
# # print("Middle Node:", ll1.middleNode(head = [1,2,3,4,5]).value)
# # print("Middle Node:", ll1.middleNode(head=[1,2,3,4,5,6]).value)
# # print()
#
# print("##################################################")
#
# print("***** has_loop method *****")
# ll2 = DoublyLinkedList(1)
# ll2.append2(2).append2(3).append2(4).append2(5).append2(6).append2(7).append2(8).append2(9)
# ll2.print_list()
#
# print(ll2.has_loop())
# print()
#
# print("##################################################")
#
# print("***** find_kth_from_end method *****")
# ll2.print_list()
# print()
# print(ll2.find_kth_from_end(1).value)
# print(ll2.find_kth_from_end(2).value)
# print(ll2.find_kth_from_end(3).value)
# print(ll2.find_kth_from_end(4).value)
# print()
#
# ll3 = DoublyLinkedList(1)
# ll3.append2(2).append2(3).append2(4).append2(5)
# ll3.print_list()
# print()
# print(ll3.find_kth_from_end(2).value)
# print(ll3.find_kth_from_end(5).value)
# # print(ll3.find_kth_from_end(6).value)
# print()
#
# print("##################################################")
#
# print("***** reverse_between method *****")
# ll3.print_list()
# print()
# ll3.reverse_between(2, 4)
# ll3.print_list()
# print()
# ll3.reverse_between(2, 4)
# ll3.print_list()
# print()
# ll3.reverse_between(1, 3)
# ll3.print_list()
# print()
# ll3.reverse_between(1, 3)
# ll3.print_list()
# print()
# ll3.reverse_between(3, 3)
# ll3.print_list()
# print()
# ll3.reverse_between(0, 4)
# ll3.print_list()
# print()
# ll3.reverse_between(0, 4)
# ll3.print_list()
# print()
#
# print("##################################################")
#
# print("***** reverseList method *****")
# ll3.print_list()
# print()
# ll3.reverseList()
# ll3.print_list()
# print()
# ll3.reverseList()
# ll3.print_list()
# print()
#
# print("##################################################")
#
# ll4 = DoublyLinkedList(3)
# ll4.append2(5).append2(8).append2(10).append2(2).append2(1)
#
# print("***** partition_list method *****")
# ll4.print_list()
# print()
# ll4 = ll4.partition_list(5)
# ll4.print_list()
# print()
# ll4.print_list()
# print()
#
# print("##################################################")
#
# ll5 = DoublyLinkedList(3).append2(5).append2(8).append2(9).append2(8).append2(1).append2(3)
#
# print("***** remove_duplicates method *****")
# ll5.print_list()
# print()
# ll5.remove_duplicates()
# ll5.print_list()
# print()
#
print("##################################################")

print("***** swap_first_last method *****")
my_linked_list.print_list()
print()
print(my_linked_list.swap_first_last())
my_linked_list.print_list()
print()

print("##################################################")

print("***** is_palindrome method *****")
my_linked_list.print_list()
print()
print(my_linked_list.is_palindrome())
my_linked_list.print_list()
print()

print("##################################################")

print("***** swap_pairs method *****")
my_linked_list = DoublyLinkedList(1)
my_linked_list.append(2).append(3).append(4)
my_linked_list.print_list()
print()
print(my_linked_list.swap_pairs())
my_linked_list.print_list()
print()

print("##################################################")
