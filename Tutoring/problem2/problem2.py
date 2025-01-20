from typing import Iterator, Iterable, Self
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
    def __init__(self):
        # add other needed constructor params and complete constructor
        pass
    
    def __next__(self) -> T:
        # return the data and advance if there is data remaining.
        # if there is no data remaining, `raise StopIteration`.
        pass

class Itibag[T](Iterable[T]):

# add necessary data
    head: Node[T] | None
    tail: Node[T] | None

    def __init__(self):
        # perform necessary initialization
        self.head = None
        self.tail = None

    def __iter__(self) -> Iterator[T]:
        # return the ItibagIterator
        pass
    
    def __reversed__(self) -> Iterator[T]:
        # return an iterable for reverse iteration
        pass

    def __len__(self) -> int:
        # return number of items
        pass

    def __str__(self) -> str:
        # return a string representation
        # iterate through list (dont use iterator object)
        lists = []
        if self.head is None:
            return f"Currently empty."
        else:
            main_node = self.head
            while main_node.next:
                lists.append(main_node.data)
                main_node = main_node.next

            for node in lists:
                print(node.data)
    
    def add(self, item: T): # O(1)
        # insert an item
        # after adding ictionary check for uniqueness
        new_node = Node(item)
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
        pass

    def clear(self):
        # remove all items
        pass


ll = Itibag()
ll.add(Node(5))
ll.add(Node(15))
ll.add(Node(52))
ll.add(Node(4))
ll.add(Node(9))
print(ll)