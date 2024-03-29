visitedList = [[]]

# this is the depth first algorithm impelementation
# it's work with the "recurcive function" method
def depthFirst(graph, currentVertex, visited):
    visited.append(currentVertex)

    for vertex in graph[currentVertex]:
        if vertex not in visited:
            depthFirst(graph, vertex, visited.copy())

    visitedList.append(visited)

    return visitedList