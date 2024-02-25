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
        if pos == 1:
            self.insert_beginning(data)
        else:
            while count <= pos:
                #print(count)
                if count == pos-1:
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
        print('First Node-->', temp.data)
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


    def del_at_pos(self,pos):
        '''
            This method deletes node at particular position
        '''
        count = 1
        temp = self.head
        prev = None
        if pos == 1:
            self.head = None
        else:
            while count <= pos:
                if count == pos:
                    prev.next = temp.next
                prev = temp
                temp = temp.next
                count = count + 1


    def is_present(self,e) -> bool:
        '''
            This method checks if e is present in list.
        '''
        temp = self.head
        is_present = False
        while temp.next is not None:
            if temp.data == e:
                is_present = True
            temp = temp.next
        return is_present   


    def count(self) -> int:
        '''
            Returns number of elements in list.
        '''
        count = 1
        temp = self.head
        while temp.next is not None:
            count = count + 1
            temp = temp.next
        return count
    

    def reverse(self) -> None:
        '''
            This method reverses the linked list.
        '''
        next_pointer, prev_pointer = None, None
        current = self.head
        while current is not None:
            next_pointer = current.next
            current.next = prev_pointer
            prev_pointer = current
            current = next_pointer
        self.head = prev_pointer



l1 = LinkedList()
l1.insert_beginning(1)
l1.push(2)
l1.push(3)
l1.push(5)
l1.push(6)
l1.push(7)
l1.push(8)
l1.insert_at_pos(4,4)
l1.print_linked_list()

print('Reversing the list now-----')
# l1.del_at_beg()
# l1.del_at_end()
# l1.del_at_pos(3)
# l1.print_linked_list()
# print(l1.is_present(10))
# print(l1.count())
l1.reverse()
l1.print_linked_list()
# l1.del_at_beg()
# l1.print_linked_list()

    