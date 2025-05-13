"""
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.
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

    def remove_nodes_using_stacks(self):
        """Using stacks"""
        stack = []
        current = self.head
        while current:
            while stack and current.data > stack[-1]:
                stack.pop()
            stack.append(current.data)
            current = current.next
        #stack.reverse()
        self.head = None
        for i in stack:
            self.insert(i)

    def print(self):
        current=self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(5)
    l1.insert(2)
    l1.insert(13)
    l1.insert(3)
    l1.insert(8)
    l1.print()
    l1.remove_nodes_using_stacks()
    l1.print()