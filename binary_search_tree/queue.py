"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
sys.path.append('../doubly_linked_list') 
from doubly_linked_list import DoublyLinkedList

sys.path.append('../stack')
from stack import Stack

# List/Array Implementation 
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        return

# DoublyLinkedList implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = DoublyLinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_head(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.remove_from_tail()
#         return


# Stack Implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = Stack()
#         self.backup_storage = Stack()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         # enqueue needs to add the value to the back/head
#         # of the queue
#         # since stack can only take from the end/tail
#         # that means to use this enqueue method I will need to
#         # first remove each queued item 1 by 1 from the front/tail
#         # until there are none left - then i can add the new value
#         # after the new value is added i can re add on the values
#         # that i took off

#         # are there any items in the queue?
#         if self.size > 0:
#             # loop through the queue storage and
#             # remove each item from the front each time saving it
#             # to my backup storage
#             i = 0
#             while i < self.size:
#                 front_queued = self.storage.pop()
#                 self.backup_storage.push(front_queued)
#                 i += 1
            
#             # after i have moved every item from the queue storage
#             # to the backup storage i can add the new value to the 
#             # storage
#             self.storage.push(value)

#             # now begins the process for putting all the queued
#             # items back into the original storage
#             for _ in range(self.backup_storage.size):
#                 self.storage.push(self.backup_storage.pop())
#         else:
#             self.storage.push(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop()
#         return