from graph import connect, Node

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

fileDir = "/Users/calvinmalagon/Documents/GitHub/Masters_Program/Tutoring/graph/map.dat"

result = reader(fileDir)

for city, connected in result.items():
    print(f"{city} is connected to: {[str(n) for n in connected.connections]}")