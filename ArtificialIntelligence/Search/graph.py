class Graph:

    def __init__(self):
        self.graph = {}
        self.costs = {}
        self.vertices_no = 0

    def get_vertex_cost(self, v):
        if v not in self.costs:
            print("Vertex", v, "does not have a cost.")
        else:
            return self.costs[v]

    def add_vertex(self, v, cost):
        if v in self.graph:
            print("Vertex ", v, " already exists.")
        else:
            self.vertices_no = self.vertices_no + 1
            self.graph[v] = []
            self.costs[v] = cost

    def add_edge(self, v1, v2, e):
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            temp = [v2, e]
            self.graph[v1].append(temp)

    def print_graph(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex, ",", vertex, " -> ", edges[0], " edge weight: ", edges[1])
