"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""

"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
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
        return self.head


    def partition_list(self, x):
        curr = self.head
        s=[]
        l=[]
        while curr:
            if x > curr.data:
                s.append(curr.data)
            else:
                l.append(curr.data)
            curr = curr.next
        self.head = None
        curr = self.head
        for i in s+l:
            self.insert(i)


    def print(self):
        current=self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(4)
    l1.insert(3)
    l1.insert(2)
    l1.insert(1)
    l1.insert(67)
    l1.insert(2)
    l1.insert(8)
    l1.print()
    l1.partition_list(3)
    l1.print()