# Node and Singly LinkedList class initialization and Basic operations.

class Node:
    '''
        Main Node class
    '''
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    '''
        Main Linked List Class
    '''
    def __init__(self) -> None:
        self.head = None

    def insert_beginning(self, data):
        '''
            This method inserts data at beginning of linked list.
        '''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def push(self,data):
        '''
            This method push data at end of linked list
        '''
        temp = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.next = None

    def insert_at_pos(self, pos, data):
        '''
            This method inserts data at particular position in linked list.
        '''
        temp = self.head
        new_node = Node(data)
        count = 1
        while count <= pos:
            #print(count)
            if count == pos:
                #print(temp.data)
                new_node.next = temp.next
                temp.next = new_node
            temp = temp.next
            count+=1


    def print_linked_list(self):
        '''
            This method prints the linked list.
        '''
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def del_at_beg(self):
        '''
            This method deletes node at the beginning
        '''
        self.head = self.head.next

    def del_at_end(self):
        '''
            This method deletes node at the end.
        '''
        temp = self.head
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None

    def del_at_pos(self):
        '''
            This method deletes node at particular position
        '''
        pass


l1 = LinkedList()
l1.insert_beginning(1)
l1.push(2)
l1.push(3)
#l1.push(4)
l1.push(5)
l1.push(6)
l1.push(7)
l1.push(8)
l1.insert_at_pos(3,4)
#l1.del_at_beg()
l1.del_at_end()
l1.print_linked_list()
# l1.del_at_beg()
# l1.print_linked_list()

    