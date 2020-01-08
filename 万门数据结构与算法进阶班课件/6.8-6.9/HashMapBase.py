from MapBase import MapBase
from random import randrange

class HashMapBase(MapBase):
    def __init__ (self, cap=11, p=109345121):
        self._table = cap * [ None ]
        self._n=0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)
        
    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)  # index
    
    def __len__ (self):
        return self._n
    
    # O(1)
    def __getitem__ (self, k):
        j = self._hash_function(k) #index
        return self._bucket_getitem(j, k)
    
    # O(1)
    def __setitem__ (self, k, v):
        j = self._hash_function(k) #index
        print("hash for", k, "is", j)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:  # keep load factor <= 0.5
            self.resize(2 * len(self._table) - 1)
           
    # O(1) 
    def __delitem__ (self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._table[j] = None
        self._n -= 1
    
    def resize(self, c):
        old = list(self.items( ))
        self._table = c * [None]
        self._n = 0
        for (k,v) in old:
            self[k] = v
        