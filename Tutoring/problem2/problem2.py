from typing import Iterator, Iterable, Self


# add necessary classes


class ItibagIterator[T](Iterator[T]):

# add any necessary data to make the iterator work

    def __init__(self):
        # add other needed constructor params and complete constructor
        pass
    
    def __next__(self) -> T:
        #return the data and advance if there is data remaining.
        # if there is no data remaining, `raise StopIteration`.
        raise StopIteration

class Itibag[T](Iterable[T]):

# add necessary data

    def __init__(self):
        # perform necessary initialization
        pass

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
        pass
    
    def add(self, item: T): # O(1)
        # insert an item
        pass
    
    def remove(self, item: T) -> T | None: # O(1)
        # remove an item and return it, or None if not found
        pass

    def clear(self):
        # remove all items
        pass