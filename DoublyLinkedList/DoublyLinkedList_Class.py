# This is the Doubly Linked List Data Structure module

# Build the Node Constractor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# Implement the DoublyLinkedList
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    # adding a new node into the last of the list
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

        return True
    
    # removing the last node from the list
    def pop(self):
        # if the length of the list is zero, we have nothing to pop
        if self.length == 0:
            return None
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1

        return temp
    
    # adding a new node into the first of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

        return True
    
    # removing the first item of the list
    def pop_first(self):
        # if the length of the list is zero, we have nothing to pop
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1

        return temp

    # build a function to get a index and return the value of that index
    def get(self, index):
        # if the entered index number was out of range, return None
        if index < 0 or index >= self.length:
            return None
        
        # if the entered index number is less than the middle of the list, start the loop from head, othervise, start from that tail to the head.
        temp = self.head
        if index < (self.length / 2):
            for _ in range(index):
                temp = temp.next

        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp
    
    # setting a value into a existing node by index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        
        return False
    
    # createing a method to insert a new node into our list
    # if the entered number of index was outta the valid range, just return False
    # if the num of index is one, use the prepend function that we built that before
    # also if the number of index was equal to the length of the list, just call the append method
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1

        return True
    
    # this is a method to remove a node by a given index
    def remove(self, index):
        # if the index number is in the invalid range of numbers, just return None
        if index < 0 or index >= self.length:
            return None
        
        # and if the index is equal to the zero just use the pop_first method which we build that before
        if index == 0:
            return self.pop_first()
        
        # also if the number of index was equal to the number of length minus one, use the pop function
        if index == (self.length - 1):
            return self.pop()
        
        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1

        return temp
    
    # just a simple method to return the number of length of the list
    def len(self):
        return self.length
    
    # removing a new using a value instead of the index number
    def remove_value(self, value):
        index = 0
        temp = self.head

        while temp is not None:
            if temp.value == value:
                break
            
            temp = temp.next
            index += 1

        return self.remove(index)