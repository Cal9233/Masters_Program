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
    # dictionary property in class method?
    # dictionary: dict[Iterable[T], Node[T]] = {}

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
        # Difference in runtime using int incrementation vs appending to list?
        result = 0
        # result = []
        current_node = self.head
        while current_node:
            result += 1
            # result.append(current_node)
            current_node = current_node.next
        # return len(result)
        return result

    def __str__(self) -> str:
        # return a string representation
        # iterate through list (dont use iterator object)
        lists = []
        if self.head is None:
            return f"Currently empty."
        else:
            main_node = self.head
            while main_node:
                lists.append(str(main_node.data))
                main_node = main_node.next

            return " -> ".join(lists)
    
    def add(self, item: T): # O(1)
        # insert an item
        # after adding dictionary check for uniqueness
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
        if self.head is None:
            return None
        
        current_node = self.head
        while current_node:
            if current_node.data == item:
                # if target node is head
                if current_node.prev is None:
                    self.head = current_node.next
                    self.head.prev = None
                else:
                    current_node.prev.next = current_node.next
                    # if target node is tail
                if current_node.next is None:
                    self.tail = current_node.prev
                    self.tail.next = None
                else:
                    current_node.next.prev = current_node.prev
                return current_node.data

            current_node = current_node.next

    def clear(self):
        # remove all items
        if self.head is None:
            return None
        else:
            current_node = self.head
            while current_node:
                current_node = current_node.next
                self.head = None
                self.tail = None



ll = Itibag()
ll.add(5)
ll.add(15)
ll.add(52)
ll.add(4)
ll.add(9)
print(f"Linked Lists: {ll}")
print(f"Total amount (len method): {len(ll)}")
print("Removing Node 52")
ll.remove(52)
print(f"Linked Lists: {ll}")
print(f"Total amount after remove(52) (len method): {len(ll)}")
ll.clear()
print(f"Linked Lists: {ll}")
print(f"Total amount after clear (len method): {len(ll)}")