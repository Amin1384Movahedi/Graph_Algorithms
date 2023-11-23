import math
import sys
from Graph.Graph_Class import Graph
from DoublyLinkedList.DoublyLinkedList_Class import DoublyLinkedList
from DepthFirst_Algorithm.DepthFirst_Class import depthFirst

    
def Dijkstra(graph, initial, endpoint):
    path = {}
    adj_node = {}
    queue = DoublyLinkedList()
    graph = graph.get_graph()
    for node in graph:
        path[node] = float(math.inf)
        adj_node[node] = None
        queue.append(node)
        
    path[initial] = 0
    while queue.length != 0:
        # find min distance which wasn't marked as current
        key_min = queue.get(0).value
        min_val = path[key_min]
        for n in range(1, queue.len()):
            if path[queue.get(n).value] < min_val:
                key_min = queue.get(n).value
                min_val = path[key_min]
        cur = key_min
        queue.remove_value(cur)
        print(cur)
        
        for i in graph[cur]:
            alternate = graph[cur][i] + path[cur]
            if path[i] > alternate:
                path[i] = alternate
                adj_node[i] = cur
                
    print('The path between A to H')
    print(endpoint, end = '<-')
    while True:
        endpoint = adj_node[endpoint]
        if endpoint is None:
            print("")
            break
        print(endpoint, end='<-')
    
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

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.weight(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

# print(graph.weight("a", "b"))

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")
print(previous_nodes)
print(shortest_path)

# Dijkstra(graph, "a", "d")