class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

    def __init__ (self):
        self._head = None
        self._size = 0
        self._current = self._head 

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        self.new_node = self.SListNode(value=value)
        if self._head is None or (self.new_node.value < self._head.value):
            temp = self._head
            self.new_node.next = temp
            self._head = self.new_node
        else:
            self.current: self.SListNode = self._head
            while self.current.next is not None and self.current.next.value <= self.new_node.value:
                self.current = self.current.next
            self.temp = self.current.next
            self.current.next = self.new_node
            self.new_node.next = self.temp
        self._size += 1
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        for item in self:
            if item.value == value:
                return item.value
        return None
                
    '''Remove the first occurance of value.'''
    def remove(self, value):
        self._current = self._head
        if self._head.value == value:
            self._head = self._head.next
        else:
            for item in self:
                if item.next is not None:
                    if item.next.value == value:
                        item.next = item.next.next
                        self._size -= 1
                        return True
        return False


    '''Remove all instances of value'''
    def remove_all(self, value):
        for item in self:
            if item.value == value:
                self.remove(value)
        

    '''Returns the size of the slist object'''
    def size(self):
        return self._size
    
    '''Convert the list to a string and return it'''
    def __str__(self):
        result = []
        for item in self:
            result.append(item.value)
        return f'{result}'

    '''testing and debugging purposes used in test modules'''
    def __repr__(self) -> str:
        result = []
        for item in self:
            result.append(item.value.number())
        return f'{result}'

    '''Return an iterator for the list'''
    def __iter__(self):
        self._current = self._head  # Reset the current node when starting an iteration
        return self

    '''implement StopIteration for the list if value is None'''
    def __next__(self):
        if self._current is None:
            raise StopIteration
        item = self._current
        self._current = self._current.next
        return item
    
    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        cnt = 0
        idx = index
        if index >= self.size():
            raise IndexError
        elif index < 0:
            idx = self.size() + index
        for item in self:
            if cnt == idx:
                return item
            cnt += 1

    def __len__(self):
        cnt = 0
        for item in self:
            cnt+=1
        return cnt