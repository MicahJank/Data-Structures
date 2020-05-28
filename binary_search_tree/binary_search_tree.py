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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # node_to_add = BSTNode(value)
        current_node = self

        # go right
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                node_to_add = BSTNode(value)
                self.right = node_to_add

        # go left
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                node_to_add = BSTNode(value)
                self.left = node_to_add

        # Traverse Right
        # if value >= self.value:
        #     while current_node.right is not None or value < current_node.value:
        #         if value >= current_node.value:
        #             current_node = current_node.right
        #         else:
        #             while current_node.left is not None or value >= current_node.value:
        #                 if value < current_node.value:    
        #                     current_node = current_node.left
        #                 else:
        #                     break
        #             else:
        #                 current_node.left = node_to_add
        #                 break
        #     else:
        #         current_node.right = node_to_add

            
        # # Traverse left
        # else:
        #     while current_node.left is not None or value >= current_node.value:
        #         if value < current_node.value:
        #             current_node = current_node.left
        #         else:
        #             while current_node.right is not None or value < current_node.value:
        #                 if value >= current_node.value:    
        #                     current_node = current_node.right
        #                 else:
        #                     break
        #             else:
        #                 current_node.right = node_to_add
        #                 break
        #     else:
        #         current_node.left = node_to_add

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False

        # current_node = self

        # while current_node.value != target:
        #     if target > current_node.value and current_node.right is not None:
        #         current_node = current_node.right
        #     elif target < current_node.value and current_node.left is not None:
        #         current_node = current_node.left
        #     else:
        #         return False
        # else:
        #     return True


    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self

        while current_node.right is not None:
            current_node = current_node.right
        
        return current_node.value



    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) # - pre order if the function runs first
        if self.left is not None:
            self.left.for_each(fn)
            # fn(self.value) # - in order if the function runs left first and then goes right
        
        if self.right:
            self.right.for_each(fn)
            # fn(self.value) # - post order if the function runs right first and then goes left


    # Stack Traversal - DFT - Depth First Traversal
    # As long as stack is not empty keep popping off the node and checking children and adding
    # them to the stack until you have traversed all nodes

    # Queue Traversal - BFT - Breadth First Traversal
    # As long as the queue is not empty keep dequeuing the node and check the children and add
    # them to the queue until you have traversed all nodes

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # make a queue
        # enqueue the node
        # as long as the queue is not empty
            # dequeue from the front of the queue, this is the current node
            # check that the kids are not None
            # enqueue the kids of the current node on the queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # make a stack
        # push the node on the stack
        # as long as the stack is not empty
            # pop off the stack, this is our current node
            # check that the kids are not None
            # put the kids of the current nod on the stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
