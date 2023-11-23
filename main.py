from Graph.Graph_Class import Graph
from DoublyLinkedList.DoublyLinkedList_Class import DoublyLinkedList
from DepthFirst_Algorithm.DepthFirst_Class import depthFirst
from Dijkstra_Algorithm.Dijkstra_method import dijkstra_algorithm
    
graph = Graph()

graph.add_vertex("Reykjavik")
graph.add_vertex("Oslo")
graph.add_vertex("London")
graph.add_vertex("Berlin")
graph.add_vertex("Moscow")
graph.add_vertex("Belgrade")
graph.add_vertex("Athens")
graph.add_vertex("Rome")


graph.add_edge("Reykjavik", "Oslo", 5, 1)
graph.add_edge("Reykjavik", "London", 4, 1)
graph.add_edge("Oslo", "Berlin", 1, 1)
graph.add_edge("Oslo", "Moscow", 3, 1)
graph.add_edge("Moscow", "Belgrade", 5, 1)
graph.add_edge("Moscow", "Athens", 4, 1)
graph.add_edge("Athens", "Belgrade", 1, 1)
graph.add_edge("Rome", "Berlin", 2, 1)
graph.add_edge("Rome", "Athens", 2, 1)

# graph.print_graph()

# print(graph)


# print(graph.weight("a", "b"))

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")
print(previous_nodes)
print(shortest_path)

# Dijkstra(graph, "a", "d")