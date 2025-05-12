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

    def remove_nth_from_end(self, pos:int):
        len = 1
        current = self.head

        while current.next:
            len+=1
            current = current.next
        if len == pos:
            self.head = None
        else:
            count = 0
            pos_from_start = len - pos
            prev = current
            current = self.head
            while count < pos_from_start:
                prev = current
                current = current.next
                count+=1
            prev.next = current.next

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
    l1.print()
    l1.remove_nth_from_end(3)
    l1.print()

        

