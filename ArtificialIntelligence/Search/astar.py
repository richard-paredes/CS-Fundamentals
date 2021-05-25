from graph import Graph
import heapq

def a_star_search(graph: Graph, start: str):
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

        current = node[1]
        if current == "G1" or current == "G2":
            print("Reached goal state of", current)
            found = True
            break
        
        visited[start] = True
        for edge in graph.graph[current]:
            neighbor = edge[0]
            weight = edge[1]
            new_cost = cost_so_far[current] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heuristic = graph.costs[neighbor]
                heapq.heappush(heap, (new_cost + heuristic, neighbor))
                came_from[neighbor] = current

    print(came_from)
    print(cost_so_far)
    print("Open:", [heapq.heappop(heap)[1] for i in heap])
    print("Closed:", [v for v in visited if visited[v]])
    print("Expanded:", "???")
    
    return found

class Node:
    def __init__(self,value,point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0
    
    def __eq__(self, value):
        return self.value == value.value
    
def aStar(graph, start):

    #The open and closed sets
    openset = set()
    closedset = set()

    current = Node(start, graph.costs[start])
    openset.add(current)

    #While the open set is not empty
    while openset:
        #Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o:o.G + o.H)
        
        if current == "G1" or current == "G2":
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        
        #Add it to the closed set
        openset.remove(current)
        closedset.add(current)
        for node in graph.graph[current.value]:
            neighbor = node[0]
            weight = node[1]
            heuristic = graph.costs[neighbor]

            #If it is already in the closed set, skip it
            if neighbor in closedset:
                continue

            #Otherwise if it is already in the open set
            if neighbor in openset:
                #Check if we beat the G score 
                new_g = current.G + weight
                if neighbor.G > new_g:
                    #If so, update the neighbor to have a new parent
                    neighbor.G = new_g
                    neighbor.parent = current
            else:
                newNode = Node(neighbor, graph.costs[neighbor])
                #If it isn't in the open set, calculate the G and H score for the neighbor
                newNode.G = current.G + weight
                newNode.H = graph.costs[neighbor]
                #Set the parent to our current item
                newNode.parent = current
                #Add it to the set
                openset.add(newNode)
            
    #Throw an exception if there is no path
    raise ValueError('No Path Found')