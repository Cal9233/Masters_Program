from typing import Self

class Node[T]:
    data: T
    connections: set[Self]
    def __init__(self, data):
        self.data = data
        self.connections = set()

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self)
    
def connect[T](a: Node[T], b: Node[T]):
    a.connections.add(b)
    b.connections.add(a)