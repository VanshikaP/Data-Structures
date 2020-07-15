"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        val = self.value
        self.prev = None
        self.next = None
        self.value = None
        return val

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.head.next = self.tail
            self.tail = new_node
            self.length += 1
            return self.head.value
        
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        
        if self.head is self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        
        if self.length is 2:
            self.head = self.tail
            self.length -= 1
            return self.tail.value

        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.head is None:
            return self.add_to_head(value)
        
        if self.length is 1:
            self.tail = ListNode(value, self.tail)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.length += 1
            return self.tail.value

        new_node = ListNode(value)
        tail_node = self.tail
        tail_node.next = new_node
        self.tail = new_node
        self.tail.prev = tail_node
        self.length += 1
        # # print list values
        # if not self.head:
        #     print('Error Error Error!')
        # current = self.head
        # print('list size', self.length)
        # while current:
        #     print('Value:', current.value)
        #     if current.next:
        #         print('Next:',current.next.value)
        #     else:
        #         print('Tail value:', self.tail.value)
        #     print('\n')
            # current = current.next

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return None
        
        if self.head is self.tail:
            self.length -= 1
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        
        val = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return val
        

            
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head:
            return False
        
        if node is self.head:
            return self.remove_from_head()
        
        if node is self.tail:
            return self.remove_from_tail()

        current = self.head

        # check to see if we're at a valid node 
        while current:
            # return True if the current node we're looking at matches our target node
            if current.value == node.value:
                # update our current node's next node's prev to the prev node
                current.next.prev = current.prev
                self.length -= 1
                return node.value
            current = current.next
        # if we've gotten here, then the target node isn't in our list
        return None
        # pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None

        if self.head is self.tail:
            return self.tail.value
        # reference to the largest value we've seen so far
        max_value = self.head.value

        # reference to our current node as we traverse the list
        current = self.head

        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
            
        return max_value