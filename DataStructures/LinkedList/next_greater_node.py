"""
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.
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

    def nex_greater_node(self):
        """Using Stacks
            This logic is not complete
        """
        stacks = []
        current = self.head
        j = 0
        while current:
            for i in range(j, len(stacks)):
                # print(stacks[i], current.data)
                if current.data > stacks[i]:
                    j = i
                    stacks[i] = current.data
                print(stacks)
            stacks.append(current.data)
            current = current.next
        current = self.head
        for i in range(len(stacks)):
            if stacks[i] == current.data:
                stacks[i] = 0
            current = current.next
        print(stacks)


    def print(self):
        current=self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(7)
    l1.insert(5)
    l1.insert(1)
    l1.insert(9)
    l1.insert(2)
    l1.insert(5)
    l1.insert(1)
    l1.print()
    l1.nex_greater_node()
    l1.print()