from typing import Iterator, Iterable, Self
# Sized implements __len__ into any type
# Sequence implements __get__ method and __len__ method into any type

# add necessary classes
class ItibagIterator[T](Iterator[T]):

# add any necessary data to make the iterator work
    def __init__(self, data: list[T], reverse: bool = False):
        # add other needed constructor params and complete constructor
        self.data = data
        self.index = len(data) - 1 if reverse else 0
        self.reverse = reverse
    
    def __next__(self) -> T:
        #return the data and advance if there is data remaining.
        # if there is no data remaining, `raise StopIteration`.
        if self.reverse:
            if self.index < 0:
                raise StopIteration
            value = self.data[self.index]
            self.index -= 1
        else:
            if self.index >= len(self.data):
                raise StopIteration
            value = self.data[self.index]
            self.index += 1
        return value

class Itibag[T](Iterable[T]):

# add necessary data

    def __init__(self):
        # perform necessary initialization
        self.data: list[T] = []
        self.set: set[T] = set()

    def __iter__(self) -> Iterator[T]:
        # return the ItibagIterator
        return ItibagIterator(self.data)
    
    def __reversed__(self) -> Iterator[T]:
        # return an iterable for reverse iteration
        return ItibagIterator(self.data, reverse = True)

    def __len__(self) -> int:
        # return number of items
        return len(self.data)

    def __str__(self) -> str:
        # return a string representation
        return f"{self.data}"
    
    def add(self, item: T): # O(1)
        # insert an item
        if item not in self.data:
            self.data.append(item)
        else:
            return f"Item {item} already exists in Itibag"
    
    def remove(self, item: T) -> T | None: # O(1)
        # remove an item and return it, or None if not found
        if item in self.data:
            self.data.remove(item)
            self.set.remove(item)
            return item
        return None

    def clear(self):
        # remove all items
        if len(self.data) > 0:
            self.data.clear()
            self.set.clear()
            return self
        
numbers = [1, 2, 3, 4, 5, 6]

i: Itibag[int] = Itibag()  # Specify type explicitly as int
i.add(12).add(15).remove(12)
print(i)  # Output: [15]