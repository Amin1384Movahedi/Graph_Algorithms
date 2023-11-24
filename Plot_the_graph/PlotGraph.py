import matplotlib.pyplot as plt
import random

# generating some random possitions based on a circle pattern
def Generate_Possition(a, b, r):
    possitions = []

    for x in range(-30, 30):
        for y in range(-30, 30):
            if (x - a) ** 2 + (y - b) ** 2 == r ** 2:
                possitions.append((x, y))

    return possitions

def Plot(graph):
    # extract the number of vertecies and the name of the each vertex
    num_of_vertecies = graph.len_vertecies()
    vertecies_names = graph.get_vertecies()

    # getting some random positions
    possitions = Generate_Possition(0, 0, 5)

    # getting more random positions if the number of generated possitions is less that the number of vertecies
    while len(possitions) <= num_of_vertecies:
        possitions.append((random.randint(0, 10), random.randint(0, 10)))

    # choose some random positions from generated possitions if the number of generated positions is greater than the number of vertecis
    if len(possitions) > num_of_vertecies:
        possitions = random.sample(possitions, num_of_vertecies)

    each_vertex_possitions = {}

    for i, vertex in enumerate(vertecies_names):
        each_vertex_possitions[vertex] = possitions[i]

    for vertex in each_vertex_possitions:
        plt.scatter(each_vertex_possitions[vertex][0], each_vertex_possitions[vertex][1])
        plt.text(each_vertex_possitions[vertex][0], each_vertex_possitions[vertex][1], vertex, va="bottom", ha="center")

        for outgoing_edges in graph.get_outgoing_edges(vertex):
            weight = graph.weight(vertex, outgoing_edges)
            x = [each_vertex_possitions[vertex][0], each_vertex_possitions[outgoing_edges][0]]
            y = [each_vertex_possitions[vertex][1], each_vertex_possitions[outgoing_edges][1]]
            mid = [(x[0] + x[1]) / 2, (y[0] + y[1]) / 2]

            plt.text(mid[0], mid[1], weight, va="bottom", ha="center")

            plt.plot(x, y)

    plt.show()