# import sys
# sys.path.append('../queue')
# from queue import Queue
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size is 0:
            return None
        else:
            val = self.storage[0]
            self.storage.remove(val)
            self.size -= 1
            return val

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            val = self.storage[self.size - 1]
            self.storage.remove(self.storage[self.size - 1])
            self.size -= 1
            return val

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        if self.right is None:
            return max_value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue
        nodes = Queue()
        # # start node with root node
        nodes.enqueue(node)
        # print('******', nodes.dequeue().value)
        # # while loop that checks size of the loop
        while nodes.size is not 0:
            # pointer variable that updates at beginning of each loop
            currentNode = nodes.dequeue()
            print(currentNode.value)

            if currentNode.left is not None:
                nodes.enqueue(currentNode.left)
            if currentNode.right is not None:
                nodes.enqueue(currentNode.right)
   

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # node.for_each(print)

        # use a stack
        stack = Stack()
        # start stack at root node
        stack.push(node)

        # while loop that checks stack size
        while stack.size is not 0:
            # pointer variable and update it
            currentNode = stack.pop()
            print(currentNode.value)

            if currentNode.left is not None:
                stack.push(currentNode.left)
            if currentNode.right is not None:
                stack.push(currentNode.right)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            self.pre_order_dft(node.left)
        if node.right is not None:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left is not None:
            self.post_order_dft(node.left)
        if node.right is not None:
            self.post_order_dft(node.right)
        print(node.value)
