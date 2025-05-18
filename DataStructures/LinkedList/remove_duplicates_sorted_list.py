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

    def remove_duplicates_sorted_list(self):
        """Using set Wrong Solution"""
        current = self.head
        s=[]
        while current:
            s.append(current.data)
            current = current.next
        s = list(set(s))
        self.head = None
        current = self.head
        for i in s:
            self.insert(i)

    def remove_duplicates_sorted_list_two_pointers(self):
        """Two pointers"""
        dummy = Node(-1)
        dummy.next = self.head
        current = self.head
        prev = dummy
        while current:
            dup = False
            while current.next and current.data == current.next.data:
                current = current.next
                dup = True
            if dup:
                #Skip all duplicates
                prev.next = current.next
            else:
                # No duplicates; move prev forward
                prev = prev.next
            current = current.next
        self.head = dummy.next

    def print(self):
        current=self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)
    l1.insert(4)
    l1.insert(4)
    l1.insert(5)
    l1.insert(5)
    l1.print()
    l1.remove_duplicates_sorted_list_two_pointers()
    l1.print()