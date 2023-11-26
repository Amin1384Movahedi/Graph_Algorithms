def encode_graph(graph):
    encoded_graph = {}
    encode = {}
    i = 1

    for vertex in graph.get_nodes():
        encode[vertex] = i 
        i += i 

    for vertex in graph.get_nodes():
        edges = []
        
        for edge in graph.get_outgoing_edges(vertex):
            edges.append(encode[edge])

        encoded_graph[encode[vertex]] = edges

    return encoded_graph

def decode_path(path):
    decoded_path = []
    decode = {}
    i = 1

    for vertex in graph.get_nodes():
        decode[i] = vertex
        i += 1

    for node in path:
        decoded_path.append(decode[node])

    return decoded_path