class Graph:
    # Build the graph's adj_list consstractor
    def __init__(self):
        self.adj_list = {}

    # print the graph by calling the print_graph() method
    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    # adding new vertex if the vertex wasn't duplicated
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = {}

            return True
        
        return False

    # adding connections or edges between the vertex by giving start vertex and ending vertex, weight of the edge and a variable that specifies the type of the connections between the two vertex
    def add_edge(self, v1, v2, weight, bidirectional=1):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if bidirectional == 1:
                self.adj_list[v1][v2] = weight
                self.adj_list[v2][v1] = weight

            else:
                self.adj_list[v1][v2] = weight

            return True
        
        return False
    
    # removing the edge between the two vertex
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)

        if v2 in self.adj_list.keys():
            self.adj_list[v2].remove(v1)
        
        return True
    
    # removing a vertex from the graph
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)

            del self.adj_list[vertex]

            return True
        
        return False
    
    # return the adj_list
    def get_nodes(self):
        return self.adj_list
    
    # return all the outgoing vertecies from the given node
    def get_outgoing_edges(self, node):
        return list(self.adj_list[node].keys())
    
    # return the weight of the edge by the given node and neighbor
    def weight(self, node, neighbor):
        return self.adj_list[node][neighbor]
    
    # return the number of vertecies in the graph
    def len_vertecies(self):
        return len(list(self.adj_list))
    
    # return the vertecies
    def get_vertecies(self):
        return list(self.adj_list.keys())