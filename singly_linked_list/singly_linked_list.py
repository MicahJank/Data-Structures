class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, current_next)


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None)
        self.length += 1

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return
        
        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value

        # self.head = self.head.next
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        print(self.tail.value)
        return value

            

    def add_to_tail(self, value):
        new_node = ListNode(value, None)
        self.length += 1

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        
        self.tail = new_node

    def remove_from_tail(self):
        value = self.tail.value
        prev_node = self.head

        # since a singly linked list has no prev option
        # i think i will have to start at the head and keep
        # going next until i get to the second to last item
        # in the list

        while prev_node.next is not self.tail:
            prev_node = prev_node.next
        
        prev_node.next = None
        self.tail = prev_node
        self.length -= 1

        return value

    def contains(self, value):
        current_node = self.head

        if not self.head:
            return False

        for num in range(self.length):
            if(current_node.value == value):
                return True
            current_node = current_node.next

    def get_max(self):
        if self.head:  
            max_value = 0
            node = self.head
            for num in range(self.length):
                if node.value > max_value:
                    max_value = node.value
                node = node.next
            return max_value
        return