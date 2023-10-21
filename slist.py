
class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

    def __init__ (self):
        self._head = None
        self._tail = None
        self._size = 0

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        self.temp = self._head
        if self._head == None:
            self._head = self.SListNode(value=value)
            self._tail = self._head
        elif value > self.temp.value:
            while value > self.temp.next.value and self.temp.next != None:
                self.temp = self.temp.next
            
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        pass

    '''Remove the first occurance of value.'''
    def remove(self, value):
        pass

    '''Remove all instances of value'''
    def remove_all(self, value):
        pass

    '''Convert the list to a string and return it'''
    def __str__(self):
        pass

    '''Return an iterator for the list'''
    def __iter__(self):
        pass

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        pass

    def __len__(self):
        pass
    