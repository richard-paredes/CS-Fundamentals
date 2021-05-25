from graph import Graph
from bfs import breadth_first_search
from dfs import depth_first_search
from ibfs import best_first_search
from astar import a_star_search, aStar

def main():
    # driver code
    graph = Graph()

    # Add vertices to the graph along with the heuristic
    graph.add_vertex("S",10)
    graph.add_vertex("C",3)
    graph.add_vertex("A",5)
    graph.add_vertex("F",9)
    graph.add_vertex("B",8)
    graph.add_vertex("G2",0)
    graph.add_vertex("G1",0)
    graph.add_vertex("D",2)
    graph.add_vertex("E",4)
    graph.add_vertex("H",2)

    # Add the edges between the vertices by specifying
    # the from and to vertex along with the edge weights.
    graph.add_edge("S", "A", 3)
    graph.add_edge("S", "F", 5)
    graph.add_edge("S", "B", 7)
    graph.add_edge("A", "C", 1)
    graph.add_edge("A", "D", 2)
    graph.add_edge("A", "E", 4)
    graph.add_edge("B", "E", 1)
    graph.add_edge("B", "G2", 9)
    graph.add_edge("C", "D", 4)
    graph.add_edge("C", "S", 2)
    graph.add_edge("D", "G1", 6)
    graph.add_edge("E", "G2", 5)
    graph.add_edge("E", "H", 1)
    graph.add_edge("F", "D", 4)
    graph.add_edge("G1", "C", 2)
    graph.add_edge("G2", "B", 8)
    # graph.print_graph()

    print("Breadth-first Search Results:")
    breadth_first_search(graph, "S")
    print()

    print("Depth-first Search Results:")
    depth_first_search(graph, "S")
    print()

    print("Best-first Search Results:")
    best_first_search(graph, "S")
    print()

    print("A* Search Results:")
    a_star_search(graph, "S")
    print()
main()
