from graph import connect, Node
from queue import Queue

# read file, 0 = not connected, 1 = connected
# line one = names of nodes
# check which nodes are connected
# function returns dictionary of connections

def reader(fileName: str) -> dict[str, Node[str]]:
    graph = {}
    with open(fileName, "r") as file:
        cities = file.readline().strip("\n").split(';')
        for city in cities:
            graph[city] = Node(city)

        for i, line in enumerate(file):
            connections = line.strip().split()

            for j, connected in enumerate(connections):
                if connected == "1":
                    connect(graph[cities[i]], graph[cities[j]])
            
    return graph

# functions (graph, starting city, ending city)
# returns all paths, shortest to longest

def travel(graph: dict[str, Node[str]], city_A: str, city_B: str):
    # shortest path, loop through cities, count amount in array, return smallest value
    # BFS explores all neighbors before progressing to deeper level
    # DFS goes as deep as possible before back tracking
    # BFS = Shortest path
    # DFS = Longest path

    paths_seen = set()
    queue = Queue()
    queue.put([city_A])
    def shortest_path(path, city):
        length = 0
        for city, connections in graph:
            pass
    
    def dfs(node, city, visited):
        if node in visited:
            return None
        if node.data == city:
            return node
        copy_v = set(visited)
        copy_v.add(node)
        for child in node.connections:
            result = dfs(child, city, copy_v)
            if result is not None:
                return result
        return None



fileDir = "/Users/calvinmalagon/Documents/GitHub/Masters_Program/Tutoring/graph/map.dat"

result = reader(fileDir)

for city, connected in result.items():
    print(f"{city} is connected to: {[str(n) for n in connected.connections]}")