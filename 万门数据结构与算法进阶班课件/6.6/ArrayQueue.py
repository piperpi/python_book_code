class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty( ):
            raise ValueError( 'Queue is empty' )
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty( ):
            raise ValueError( 'Queue is empty' )
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = e
        self._size += 1
        
    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
        
    def print(self):
        for i in range(self._size):
            pos = (self._front + self._size - 1 - i) % len(self._data)
            #print(str(i), ": ", str(pos))
            print(self._data[pos])        

if __name__ == "__main__":        
    myqueue = ArrayQueue()
    print ('size was: ', str(len(myqueue)))
    myqueue.enqueue(1)
    myqueue.enqueue(2)
    myqueue.enqueue(3)
    myqueue.enqueue(4)
    myqueue.enqueue(5)
    print ('size was: ', str(len(myqueue)))
    myqueue.print()
    myqueue.dequeue()
    myqueue.dequeue()
    print ('size was: ', str(len(myqueue)))
    myqueue.print()
    myqueue.enqueue(6)
    myqueue.enqueue(7)
    myqueue.dequeue()
    myqueue.dequeue()
    print ('size was: ', str(len(myqueue)))
    myqueue.print()
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.dequeue()
    print ('size was: ', str(len(myqueue)))
    myqueue.print()
    #myqueue.dequeue()