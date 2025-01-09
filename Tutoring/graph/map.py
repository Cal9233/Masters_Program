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

    # BFS 
    def shortest_path(graph, city_A, city_B):
        paths_seen = set()
        queue = Queue()
        queue.put([city_A])

        while queue:
            current_path = queue.get()
            current_city = current_path[-1]

            if current_city.data == city_B.data:
                return len([node.data for node in current_path])

            if current_city in paths_seen:
                continue

            paths_seen.add(current_city)

            for neighbor in current_city.connections:
                if neighbor not in paths_seen:
                    new_path = current_path + [neighbor]
                    queue.put(new_path)
        return None
    
    # DFS
    def longest_path(graph, city_A, city_B):
        all_paths = []
        paths_visited = set()

        def dfs(node, path):
            if node.data == city_B:
                all_paths.append(path[:])
                return
            paths_visited.add(node)
            
            for child in node.connections:
                if child not in paths_visited:
                    dfs(child, path + [child])
            
            paths_visited.remove(node)
    
        start = graph[city_A]
        dfs(start, [start])

        if all_paths:
            return [node.data for node in max(all_paths, key=len)]
        return None
    
    short_path = shortest_path(graph, city_A, city_B)
    long_path = longest_path(graph, city_A, city_B)

    if short_path:
        print(f"Shortest path from {city_A} to {city_B}: {' -> '.join(short_path)}")
        print(f"Length: {len(short_path)} cities")
    else:
        print(f"No path found from {city_A} to {city_B}")

    if long_path:
        print(f"Longest path from {city_A} to {city_B}: {' -> '.join(long_path)}")
        print(f"Length: {len(long_path)} cities")
    


fileDir = "/Users/calvinmalagon/Documents/GitHub/Masters_Program/Tutoring/graph/map.dat"

result = reader(fileDir)

for city, connected in result.items():
    print(f"{city} is connected to: {[str(n) for n in connected.connections]}")

travel(result, 'Austin', 'Tokyo')