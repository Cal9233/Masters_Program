from typing import Iterator, Iterable, Self
from stringbuilder import StringBuilder
# Sized implements __len__ into any type
# Sequence implements __get__ method and __len__ method into any type

# An iterable is any object that can return an iterator, such as lists, strings, or dictionaries.
class Node[T]:
    data: T
    next: Self | None # Can't reference Node inside, so use Self
    prev: Self | None

    def __init__(self, data: T):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

# add necessary classes
class ItibagIterator[T](Iterator[T]):

# add any necessary data to make the iterator work
    def __init__(self, starting_node: Node[T] | None, reverse: bool = False):
        # add other needed constructor params and complete constructor
        self.current = starting_node
        self.reverse = reverse
    
    def __next__(self) -> T:
        # return the data and advance if there is data remaining.
        # if there is no data remaining, `raise StopIteration`.
        if self.current is None:
            raise StopIteration
        data = self.current.data
        if self.reverse is True:
            self.current = self.current.prev
        else:
            self.current = self.current.next
        return data

class Itibag[T](Iterable[T]):

# add necessary data
    head: Node[T] | None
    tail: Node[T] | None
    # dictionary property in class method?
    dictionary: dict[T, Node[T]]

    def __init__(self):
        # perform necessary initialization
        self.head = None
        self.tail = None
        self.dictionary = {}

    def __iter__(self) -> Iterator[T]:
        # return the ItibagIterator
        return ItibagIterator(starting_node = self.head)
    
    def __reversed__(self) -> Iterator[T]:
        # return an iterable for reverse iteration
        return ItibagIterator(starting_node = self.tail, reverse = True)

    def __len__(self) -> int:
        # return number of items
        return len(self.dictionary)

    def __str__(self) -> str:
        # return a string representation
        # dictionary does not maintain order
        if self.head is None:
            return "[]"
        if self.head.next is None:
            return f"[{self.head.data}]"
        
        sb = StringBuilder()
        sb.append("[")

        curr_node = self.head

        while curr_node is not self.tail:
            assert(curr_node is not None) # curr_node cannot be None because head was not None and all nodes except tail have NONE None next
            sb.append(curr_node.data)
            sb.append(", ")
            curr_node = curr_node.next
        
        assert(curr_node is not None) # curr_node is tail
        sb.append(curr_node.data)

        sb.append("]")
        return str(sb)
    
    def add(self, item: T): # O(1)
        # insert an item
        # after adding dictionary check for uniqueness
        if item in self.dictionary:
            return
        
        new_node = Node(item)
        self.dictionary[item] = new_node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert(self.tail is not None)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove(self, item: T) -> T | None: # O(1)
        # remove an item and return it, or None if not found
        if item not in self.dictionary:
            return None
        
        node = self.dictionary[item]
        del self.dictionary[item]

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        return node.data

    def clear(self):
        # remove all items
        # clear dictionary AND linked lists
        self.dictionary.clear()
        self.head = None
        self.tail = None