from util.Empty import Empty
from util.Outbound import Outbound

class Node:
    def __init__ (self, value = None, next = None):
        self.value = value
        self.next = next
        

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.length = 0
        self.tail = self.head

    def peek(self):
        if not self.head.next:
            raise Empty( 'LinkedList is empty' )
        return self.head.next

    def get_first(self):
        if not self.head.next:
            raise Empty( 'LinkedList is empty' )
        return self.head.next
        
    def get_last(self):
        if not self.head.next:
            raise Empty( 'LinkedList is empty' )
        node = self.head
        while node.next != None:
            node = node.next
        return node
    
    def get(self, index):
        if (index < 0 or index >= self.length):
            raise Outbound( 'index is out of bound' );
        if not self.head.next:
            raise Empty( 'LinkedList is empty' )
        node = self.head.next
        for i in range(index):
            node = node.next
        return node
                
    def add_first(self, value):
        node = Node(value, None)
        node.next = self.head.next
        self.head.next = node
        self.length += 1   
        
    def add_last(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = self.tail.next
        self.length += 1   
        
    def remove_first(self):
        if not self.head.next:
            raise Empty( 'LinkedList is empty' )
        value = self.head.next.value
        self.head.next = self.head.next.next
        self.length -= 1
        return value    
        
    def remove_last(self):
        if not self.head.next:
            raise Empty( 'LinkedList is empty' )
        node = self.head.next
        prev = self.head
        while node.next != None:
            prev = node
            node = node.next
        prev.next = None
        return node.value

    def printlist(self):
        node = self.head.next
        count = 0
        while node and count<20:
            print(node.value, end = " ")
            node = node.next
            count = count + 1
        print('')
        
    def size(self):
        return self.length