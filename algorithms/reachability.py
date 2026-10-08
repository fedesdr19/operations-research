"""
Reachability Algorithm (Breadth-First Search):
Finds all nodes reachable from a given starting node in a directed graph.

Graph: Adjacency list (dictionary of nodes and their successors).
Data structures:
    Q: Queue of nodes waiting to be explored (list).
    M: List of nodes already explored.
Assumptions:
    - The starting node exists in the graph.
    - All referenced nodes exist in the graph.
Time complexity:
    O(n^2 + mn), where n is the number of nodes and m is the number of arcs.
    Q.pop(0) takes O(n) because removing the first element shifts the remaining elements.
    Membership checks in Q and M take O(n) in the worst case.
    List append operations take O(1) amortized [=occasional resizing costs are spread across many append operations].
    Each node is explored at most once, and each arc is examined at most once.
"""

graph = {
    1: [2,4],
    2: [3], 
    3: [4,5],
    4: [2,5],
    5: [4]
}
start = 1

Q = [start]	#queue of nodes waiting to be explored
M = []

while Q:	#at most n
        u = Q.pop(0)												#O(n): remove the first node from Q
        
        M.append(u)													#O(1) amortized: add the explored node to M
        for successor in graph[u]:									#O(out-degree(u)); O(m) iterations in total
              if successor not in Q and successor not in M:			#O(n)+O(n) = O(n)
                   Q.append(successor)								#O(1) amortized
        print("u =", u)
        print("Q =", Q)
        print("M =", M)
        print()