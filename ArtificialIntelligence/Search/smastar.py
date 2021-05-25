from graph import Graph
import heapq

def simplified_memory_bounded_a_star_search(graph: Graph, start: str):
    visited = { v : False for v in graph.graph }

    came_from = {}
    cost_so_far = {}
    heap = []
    closed = []

    heapq.heappush(heap, (0, start))
    came_from[start] = None
    cost_so_far[start] = 0

    found = False
    while heap:
        node = heapq.heappop(heap)

    print("Open:", [heapq.heappop(heap)[1] for i in heap])
    print("Closed:", [v for v in visited if visited[v]])
    print("Expanded:", "???")
    
    return found