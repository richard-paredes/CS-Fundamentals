from graph import Graph
import heapq

def best_first_search(graph: Graph, start: str):
    visited = { v : False for v in graph.graph }

    heap = []
    closed = []
    heapq.heappush(heap, (graph.costs[start], start))

    found = False
    while heap:
        node = heapq.heappop(heap)
        
        current = node[1]
        if current == "G1" or current == "G2":
            print("Reached goal state of", current)
            found = True
            break

        visited[current] = True
        for edge in graph.graph[current]:
            neighbor = edge[0]
            weight = edge[1]
            if visited[neighbor] == False and neighbor not in heap:
                heapq.heappush(heap, (graph.costs[neighbor], neighbor))
    
    print("Open:", [heapq.heappop(heap)[1] for i in range(len(heap))])
    print("Closed:", [v for v in visited if visited[v]])
    print("Expanded:", "???")
    return found
    