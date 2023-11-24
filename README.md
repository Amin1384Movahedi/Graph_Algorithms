# Graph_Algorithms

here i built a graph data structure that take some vertecies, i used the cities names in here.<br />
it's also takes edges with weights that tells the distance between two vertecies, it's has an option that tells the edges is bidirectional or not

# Depth First Search (DFS)

Depth-first search is an algorithm for traversing or searching tree or graph data structures. <br />
The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.<br /><br />

we have a mothod which is called depthFirst(), it's worked with the recurcive algorithm<br />
it's takes the graph, a starting node and a empty list then the function return a list that include all of the possible pathes which is starts from the given starting node.<br />

# Dijstra's Algorithm

![Dijkstra Algorithm](https://github.com/Amin1384Movahedi/Graph_Algorithms/blob/main/assets/Dijkstra.gif)

   1. Mark the source node with a current distance of 0 and the rest with infinity.
   2. Set the non-visited node with the smallest current distance as the current node.
   3. For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge connecting 0->1. If it is smaller than the current distance of Node, set it as the new current distance of N.
   4. Mark the current node 1 as visited.
   5. Go to step 2 if there are any nodes are unvisited.

The algorithm maintains a set of visited vertices and a set of unvisited vertices.<br /> 
It starts at the source vertex and iteratively selects the unvisited vertex with the smallest tentative distance from the source.<br /> 
It then visits the neighbors of this vertex and updates their tentative distances if a shorter path is found.<br /> 
This process continues until the destination vertex is reached, or all reachable vertices have been visited.<br />

# Plot the graph with matplotlib

![Graph Plotting](https://github.com/Amin1384Movahedi/Graph_Algorithms/blob/main/assets/PlottedGraph.png)

there is a function that called PlotGraph<br />
it's just take the graph, then it's generate some random possitions in a circle pattern for each vertex<br />
then plot these dots with scatter method in matplotlib and labelling them by each vertex's name<br />
after that, it's draw each edges between the vertecies with plot method in matplotlib and label each edge or connections with the weights of them.<br />
 
