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

    def traverse_in_reverse(self, node):
        if node is None:
            return None
        self.traverse_in_reverse(node.next)
        print(node.data)


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
    l1.traverse_in_reverse(l1.head)
    #l1.prin#t()