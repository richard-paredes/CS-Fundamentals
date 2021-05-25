from graph import Graph

def breadth_first_search(graph: Graph, start: str):
    visited = { v : False for v in graph.graph }

    queue = []
    closed = []
    queue.append(start)

    found = False
    while queue:
        current = queue.pop(0)
        
        if current == "G1" or current == "G2":
            found = True
            print("Reached goal state of", current)
            break

        visited[current] = True
        closed.append(current)
        for edge in sorted(graph.graph[current]):
            neighbor = edge[0]
            weight = edge[1]

            if visited[neighbor] == False and neighbor not in queue:
                queue.append(neighbor)
        
    print("Open:", queue)
    print("Closed:", closed)
    print("Expanded:", "???")
    return found