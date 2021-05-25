from graph import Graph

def depth_first_search(graph: Graph, start: str):
    visited = { v : False for v in graph.graph }
    
    stack = []
    closed = []
    stack.append(start)
    
    found = False
    while stack:
        current = stack.pop()
        visited[current] = True

        if current == "G1" or current == "G2":
            print("Reached goal state of", current)
            found = True
            break
            
        # need to reverse since we pop the last item from stack to go deeper
        for edge in sorted(graph.graph[current], reverse = True):
            neighbor = edge[0]
            weight = edge[1]

            # isClosed = True
            # for v in graph.graph[vertex]:
            #     if not visited[v[0]]:
            #         isClosed = False
            #         break
            # if isClosed:
            #     closed.append(vertex)
            if visited[neighbor] == False and neighbor not in stack:
                stack.append(neighbor)
        
    print("Open:", stack)
    print("Closed:", [v for v in visited if visited[v]])
    print("Expanded:", "???")
    return found