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
Time complexity (expected):
    S is a set: hashing allows O(1) membership checks on average, unlike a list, which requires a linear search taking O(n) in the worst case.
    This reduces the expected overall complexity from O(n^3) to O(n^2).
    However, hash collisions can make set membership O(n) in the worst case, so O(n^2) is an expected bound, not a strict worst-case guarantee.
    O(n^2) = O(n) iterations* (  (O(n) for minimum search) +  (O(n) for each neighbour * O(1) for search in S)  )
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



S = {source}

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
    S.add(node)
    result[node] = ( temp[node][0], temp[node][1])
    del temp[node]
    
    for near_node, cost in nodes[node]:							#update cost of neighbours only if they aren't in S and the path is shorter
                                                                #Time complexity: O(n) (number of edges from each node: at worst (n-1) neighbours)
        if near_node in S:	#Time complexity: O(1)
            continue
        if near_node in temp and temp[near_node][0] <= minimum[1][0] + cost:
            continue
        temp[near_node] = (minimum[1][0] + cost, node)
   
print("Result:", result)
 