from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.connections = set()

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self)
    
def connect(a, b):
    a.connections.add(b)
    b.connections.add(a)

def find_path(start_node, end_data):
    queue = Queue()
    queue.put([start_node])

    while queue.not_empty:
        path = queue.get()
        node = path[-1]
        if node.data == end_data:
            return path
        for connection in node.connections:
            if connection not in path:
                new_path = list(path)
                new_path.append(connection)
                queue.put(new_path)
        
    return None

# Nodes
start = Node("start")
starbucks = Node("starbucks")
bk = Node("bk")
target = Node("target")
mcdonalds = Node("mconalds")
buckys = Node("buckys")
wendys = Node("wendys")

# connect
start.connections.add(bk)
start.connections.add(mcdonalds)
start.connections.add(wendys)
mcdonalds.connections.add(buckys)
mcdonalds.connections.add(target)
wendys.connections.add(starbucks)
target.connections.add(starbucks)

find = find_path(start, starbucks.data)
print(find)


# find all routes through connections