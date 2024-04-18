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
        #print('First Node-->', temp.data)
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
            This method reverses the linked list using three pointers.
        '''
        next_pointer, prev_pointer = None, None
        current = self.head
        while current is not None:
            next_pointer = current.next
            current.next = prev_pointer
            prev_pointer = current
            current = next_pointer
        self.head = prev_pointer

    def del_alt_node(self):
        """
            This method deletes alternate nodes
        """
        prev = self.head
        prev_next = self.head.next
        while prev is not None and prev_next is not None:
            prev.next = prev_next.next
            prev_next = None
            prev = prev.next
            if prev is not None:
                prev_next = prev.next

    def add_one_to_list(self):
        """
            Add 1 to list = 1->9->9 becomes 2->0->0
        """
        temp = self.head
        num = 0
        while temp is not None:
            num = num * 10 + temp.data
            temp = temp.next
        num = num + 1
        for i in [int(x) for x in str(num)]:
            self.push(i)

    def add_two_int_lists(self,second):
        """
            add 2 lists = 1->0->0 and 5->0 becomes 1->5->0
        """
        num1, num2 = 0,0
        first = self.head
        sec = second.head
        while first is not None:
            num1 = num1 * 10 + first.data
            first = first.next
        while sec is not None:
            num2 = num2 * 10 + sec.data
            sec = sec.next
        num3 = num1 + num2
        l = LinkedList()
        for i in [int(x) for x in str(num3)]:
            l.push(i)
        return l
    
    def pairwise_swap_nodes(self):
        """
            This method swaps pairwise data.
        """
        temp = self.head
        temp1 = self.head.next
        if temp is None:
            return
        while temp and temp1:
            temp.data, temp1.data = temp1.data, temp.data
            # print(temp.data)
            # print(temp1.data)
            temp = temp1.next
            if temp is not None:
                temp1 = temp.next

    def remove_duplicates(self):
        """
            This method removes duplicates from linkedlist.
        """
        temp = self.head
        prev = None
        my_set = set()
        while temp:
            if temp.data in my_set:
                prev.next = temp.next
            else:
                my_set.add(temp.data)
                prev = temp
            temp = temp.next

    def detect_loop(self):
        """
            This method detects if there is any loop in linked list.
        """
        temp = self.head
        if temp or temp.next:
            return False
        
       


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_beginning(1)
    l1.push(1)
    l1.push(1)
    l1.push(2)
    l1.push(3)
    l1.push(3)
    l1.push(4)
    # l1.push(6)
    l1.print_linked_list()
    print('----------')
    # l1.pairwise_swap_nodes()
    # l1.print_linked_list()
    l1.remove_duplicates()
    l1.print_linked_list()
    # print('---------------')
    # l2 = LinkedList()
    # l2.insert_beginning(5)
    # l2.push(0)
    # l2.print_linked_list()
    # l = l1.add_two_int_lists(l2)
    # print('---------------')
    # l.print_linked_list()
    # l1.add_one_to_list()
    # l1.print_linked_list()

    #print('Reversing the list now-----')
    # l1.del_at_beg()
    # l1.del_at_end()
    # l1.del_at_pos(3)
    # l1.print_linked_list()
    # print(l1.is_present(10))
    # print(l1.count())
    #l1.reverse()
    #l1.print_linked_list()
    # l1.del_at_beg()
    # l1.print_linked_list()

    