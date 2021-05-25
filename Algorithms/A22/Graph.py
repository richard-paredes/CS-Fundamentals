#  File: Graph.py

#  Description: Creates a graph object with helper functions

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 04/27/19

#  Date Last Modified: 04/27/19

# stack for dfs in graph
class Stack (object):

    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len (self.stack))

# queue for bfs in graph
class Queue (object):

    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check item at front of queue
    def peek (self):
        return (self.queue[0])

    # check if the queue is empty
    def is_empty (self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len(self.queue))

    def __str__ (self):
        return str(self.queue)

# vertex object for graph
class Vertex (object):

    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited

    # determine the label of the vertex
    def get_label (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str(self.label)

# graph containing vertices and connecting edges
class Graph (object):

    def __init__ (self):
        # list of vertex objects
        self.vertices = []
        # adjacency matrix
        self. adjMat = []
        # length of graph
        self.num_vertices = 0
        # determins if graph is directed
        # self.is_directed = False

    # check if a vertex is already in the graph
    def has_vertex (self, label):
        # loop through vertices sequentially
        for i in range(self.num_vertices):
            # test for matching
            if (label == (self.vertices[i].get_label())):
                return True

        return False

    # returns a vertex based on an index
    # (helper for get_neighbors to be clearer)
    def get_vertex (self, index):
        return self.vertices[index]

    # get a copy of the list of Vertex objects
    def get_vertices (self):
        return self.vertices[:]

    # given a label, get the index of a vertex
    def get_index (self, label):
        # loop through vertices sequentially
        for i in range (self.num_vertices):
            # if found, return index
            if (label == (self.vertices[i].get_label())):
                return i
        # not found
        return -1

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        # check if vertices exist in graph
        if (self.has_vertex(fromVertexLabel) and self.has_vertex(toVertexLabel)):
            fromVertexIndex = self.get_index(fromVertexLabel)
            toVertexIndex = self.get_index(toVertexLabel)
            return self.adjMat[fromVertexIndex][toVertexIndex]

        return -1

    # get a list of immediate neighors (vertex objects) that you
    # can go to from a vertex; return an empty list if there are none
    def get_neighbors (self, vertexLabel):
        neighbors = []
        # check if the given vertex is in the graph
        if (self.has_vertex(vertexLabel)):
            vertex_index = self.get_index(vertexLabel)
            for i in range(len(self.adjMat[vertex_index])):
                # if there is an edge, add it to neighbors
                if (self.adjMat[vertex_index][i] > 0):
                    vertex = self.get_vertex(i)
                    neighbors.append(vertex)

        return neighbors

    # add a vertex with a given label to the graph
    def add_vertex (self, label):
        if (not self.has_vertex(label)):
            self.vertices.append(Vertex(label))
            self.num_vertices += 1

            # add a new column in adjacency matrix
            for i in range (self.num_vertices - 1):
                (self.adjMat[i]).append(0)

            # add a new row for the new vertex
            new_row = []
            for i in range (self.num_vertices):
                new_row.append(0)
            self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        # self.is_directed = True
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # delete an edge from the adjacency matrix
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        if (self.has_vertex(fromVertexLabel) and self.has_vertex(toVertexLabel)):
            from_vertex_index = self.get_index(fromVertexLabel)
            to_vertex_index = self.get_index(toVertexLabel)
            # scenario of undirected graph:
            if (self.adjMat[from_vertex_index][to_vertex_index] == self.adjMat[to_vertex_index][from_vertex_index]):
                self.adjMat[from_vertex_index][to_vertex_index] = 0
                self.adjMat[to_vertex_index][from_vertex_index] = 0
            #scenario of a directed graph
            else:
                self.adjMat[from_vertex_index][to_vertex_index] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        # check if the vertex is in the graph
        if (self.has_vertex(vertexLabel)):
            # acquire the index of the vertex object
            vertex_index = self.get_index(vertexLabel)
            # remove the row in adjacency matrix
            self.adjMat.pop(vertex_index)
            # remove the columns in adjacency matrix
            self.num_vertices -= 1
            for i in range(self.num_vertices):
                self.adjMat[i].pop(vertex_index)
            # delete the vertex object from the graph
            self.vertices.pop(vertex_index)


    # return an unviisted vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        # looping through vertices
        for i in range(self.num_vertices):
            # finding unvisited adjacent vertex
            if (self.adjMat[v][i] > 0) and (not self.vertices[i].was_visited()):
                return i

        return -1

    # do depth first search in a graph
    def dfs (self, v):
        # create a stack
        stack = Stack()

        # mark the vertex v as visited and push it on the stack
        self.vertices[v].visited = True
        print (self.vertices[v])
        stack.push(v)

        # visit the other vertices according to depth
        while (not stack.is_empty()):
            # get an adjacent unvisited vertex
            unvisited = self.get_adj_unvisited_vertex(stack.peek())

            if (unvisited == -1):
                unvisited = stack.pop()

            else:
                (self.vertices[unvisited]).visited = True
                print (self.vertices[unvisited])
                stack.push(unvisited)

        # the stack is empty, let us reset the flags
        for i in range(self.num_vertices):
            (self.vertices[i]).visited = False

    # do breadth first search in graph
    def bfs (self, v):
        # create a queue
        queue = Queue()
        self.vertices[v].visited = True
        print(self.vertices[v])

        queue.enqueue(v)

        while (not queue.is_empty()):
            next_vertex = self.get_adj_unvisited_vertex(queue.peek())

            if (next_vertex == -1):
                queue.dequeue()

            else:
                (self.vertices[next_vertex]).visited = True
                print (self.vertices[next_vertex])
                queue.enqueue (next_vertex)


        # the queue is empty, let us reset the flags
        for i in range(self.num_vertices):
            (self.vertices[i]).visited = False

def main():
    # create a graph
    cities = Graph()

    # open file
    in_file = open("./graph.txt", "r")

    # read the number of vertices
    num_vertices = int ((in_file.readline()).strip())

    # add vertices to the list
    for i in range (num_vertices):
        city = (in_file.readline()).strip()
        cities.add_vertex(city)

    # read the edges and add them to adjacency matrix
    num_edges = int ((in_file.readline()).strip())

    for i in range (num_edges):
        edge = in_file.readline().strip()
        # print(edge)
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_undirected_edge (start, finish, weight)

    # read the line starting vertex for dfs and bfs
    start_vertex = (in_file.readline()).strip()

    # get the index of the starting vertex
    start_index = cities.get_index (start_vertex)

    # do the depth first search
    print ("Depth First Search")
    cities.dfs (start_index)

    # do the breadth first search
    print ("\nBreadth First Search")
    cities.bfs (start_index)
    print()

    print("Deletion of an edge")
    cities.delete_edge('Dallas', 'Atlanta')
    print()

    # printing adjacency matrix:
    print ("Adjacency Matrix")
    for i in range(cities.num_vertices):
        for j in range(cities.num_vertices - 1):
            print(cities.adjMat[i][j], end = ' ')
        print(cities.adjMat[i][cities.num_vertices - 1])

    print()

    print('Deletion of a vertex')
    cities.delete_vertex('Denver')
    print()

    print('List of Vertices')
    vertices = cities.get_vertices()
    for city in vertices:
        print(city)
    print()

    # printing adjacency matrix:
    print ("Adjacency Matrix")
    for i in range(cities.num_vertices):
        for j in range(cities.num_vertices - 1):
            print(cities.adjMat[i][j], end = ' ')
        print(cities.adjMat[i][cities.num_vertices - 1])

    print()
    #close file
    in_file.close()

if __name__ == "__main__":
    main()

