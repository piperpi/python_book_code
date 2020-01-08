from LinkedList import LinkedList
from LinkedList import Node

class LinkedStack(object):
    def __init__ (self):
        self._list = LinkedList()
        
    def __len__ (self):
        return self._list.length
    
    def is_empty(self):
        return self._list.length == 0
    
    # O(1)
    def push(self, e):
        self._list.add_first(e);
        
    # O(1)
    def top(self):
        return self._list.get_first().value;
    
    # O(1)
    def pop(self):
        return self._list.remove_first().value;
        
    def print(self):
        self._list.printlist()
