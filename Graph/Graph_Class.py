class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = {}

            return True
        
        return False

    def add_edge(self, v1, v2, weight, bidirectional=1):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if bidirectional == 1:
                self.adj_list[v1][v2] = weight
                self.adj_list[v2][v1] = weight

            else:
                self.adj_list[v1][v2] = weight

            return True
        
        return False
    

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)

            return True
        
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)

            del self.adj_list[vertex]

            return True
        
        return False
    
    def get_nodes(self):
        return self.adj_list
    
    def get_outgoing_edges(self, node):
        return list(self.adj_list[node].keys())
    
    def weight(self, node, neighbor):
        return self.adj_list[node][neighbor]