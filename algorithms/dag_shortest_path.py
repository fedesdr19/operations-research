"""
DAG Shortest Path Algorithm (Dynamic Programming):
Computes the shortest-path costs from node 1 to all other nodes in a Directed Acyclic Graph (DAG).

Graph: Weighted adjacency list (dictionary).
Data structures:
    L: Minimum cost of reaching each node from node 1.
    predecessor: Previous node on the shortest path.
Assumptions:
    - Nodes are numbered from 1 to n in topological order.
    - All nodes are represented in the graph.
    - The starting node is 1.
Time complexity:
    O(nm), where n is the number of nodes and m is the number of arcs.
    For each node i, the algorithm examines the outgoing arcs of all preceding nodes j < i.
"""

nodes = {
    1: [(2, 4), (3, 2), (5, 7)],
    2: [(3, 1), (4, 5)],
    3: [(4, 8), (5, 3)],
    4: [(5, 2), (6, 6)],
    5: [(6, 4)],
    6: []
}
positive_infinity = float('inf')


L = [0]								#index0 minimum cost to node1. Index1 minimum cost to node2. And so on...
predecessor = [1]                   #index0 predecessor of node1. Index1 predecessor of node2 and so on...

for i in range(2,len(nodes)+1):
    minimum = positive_infinity
    temp = None
    for j in range(1,i):
        for destination, cost in nodes[j]:
            if destination == i:
                if (L[j-1]+ cost) < minimum:
                    minimum = (L[j-1]+ cost)
                    temp = j
    L.append(minimum)
    predecessor.append(temp)
    
print("Min costs:", L)
print("Predecessor:", predecessor)