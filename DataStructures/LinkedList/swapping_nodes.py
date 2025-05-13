"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""

from typing import Generic, TypeVar, Optional

T  = TypeVar('T')

class Node(Generic[T]):

    def __init__(self, data:T, next: Optional['Node[T]']=None):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self):
        self.head: Optional[Node[T]] = None

    def insert(self, data: T) -> None:
        """
            Insert at last
        """ 
        new_node = Node(data)
        current = self.head
        if self.head is None:
            self.head = new_node
        else:
            while current.next:
                current = current.next
            current.next = new_node

    def swap(self, pos):
        """kth-node from beginning and len-kth node from beginning"""
        len = 1
        current = self.head
        while current.next:
            len+=1
            current = current.next
        # print(len)
        if len == pos:
            self.head = None
        elif pos == int(len/2) + 1 and (len%2 != 0):
            # print(pos, len)
            return
        else:
            # print(len)
            count_kth = 1
            count_len_kth = 1
            kth_node_pos_from_end = len - pos
            kth_node = self.head
            len_kth_node = self.head
            while count_kth < pos:
                count_kth +=1
                kth_node = kth_node.next
            # print(kth_node.data)
            while count_len_kth <= kth_node_pos_from_end:
                count_len_kth += 1
                len_kth_node = len_kth_node.next
            # print(pos)
            # print(count_kth)
            # print(count_len_kth)
            kth_node.data, len_kth_node.data = len_kth_node.data, kth_node.data 




    def print(self):
        current=self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert("Hello")
    l1.insert("Wow")
    l1.insert("Sarthak")
    l1.insert("Great")
    l1.insert("Hi")
    l1.insert("HeHe")
    l1.insert("HaHa")
    l1.print()
    l1.swap(2)
    l1.print()