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

    # extracting x and y from possition tuple
    x = []
    y = []

    for i in possitions:
        x.append(i[0])
        y.append(i[1])

    plt.scatter(x, y)

    # label each of point with vertex's name
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi, yi, vertecies_names[i], va='bottom', ha='center')

    plt.show()