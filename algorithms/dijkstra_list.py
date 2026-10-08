"""
Dijkstra's Shortest Path Algorithm:
Finds shortest paths from a source node in a weighted graph with non-negative edge costs.

Graph: Adjacency list (dictionary of neighbour-cost pairs).
Data structures:
    S: Nodes with finalized shortest distances.
    temp: Candidate nodes -> (tentative distance, predecessor).
    result: Finalized nodes -> (shortest distance, predecessor).
Assumptions:
    - Non-negative edge costs.
    - All referenced nodes exist in the graph.
    - Unreachable nodes are omitted from result.
Time complexity (assuming average-case O(1) dictionary operations):
    O(n^2 + mn), where n is the number of nodes and m is the number of arcs.
    For dense graphs, this becomes O(n^3).
    S is a list: membership checks require a linear search, taking O(n) in the worst case.
    In contrast, a set uses hashing to achieve O(1) membership on average, reducing the expected complexity to O(n^2) for simple graphs.
"""

nodes = {
    1: [(2, 4), (3, 2), (5, 7)],

    2: [(1, 4), (3, 1), (4, 5)],

    3: [(1, 2), (2, 1), (4, 8), (5, 3)],

    4: [(2, 5), (3, 8), (5, 2), (6, 6)],

    5: [(1, 7), (3, 3), (4, 2), (6, 4)],

    6: [(4, 6), (5, 4)]
}
source = 3		#choose the node you want to start with



S = [source]

len_nodes= len(nodes)

temp = {}
for near_node, cost in nodes[source]:
    if near_node == source:
        continue
    temp[near_node] = (cost, source)
    
result = {source: (0, source)}


while len(S) < len_nodes:										#Time complexity: O(n)
    if not temp:												#if temp is empty due to disconnected nodes exit
        break
    minimum = min(temp.items(), key=lambda x: x[1][0])			#choose the node with minimun cost in temp
                                                                #Time complexity: O(n) [n = number of nodes]
    node = minimum[0]
    S.append(node)
    result[node] = ( temp[node][0], temp[node][1])
    del temp[node]
    
    for near_node, cost in nodes[node]:							#update cost of neighbours only if they aren't in S and the path is shorter
                                                                #Time complexity: O(degree(node)), at most O(n) in a simple graph
        if near_node in S:										#Time complexity: O(n)
            continue
        if near_node in temp and temp[near_node][0] <= minimum[1][0] + cost:
            continue
        temp[near_node] = (minimum[1][0] + cost, node)
   
print("Result:", result)
 