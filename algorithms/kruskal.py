
nodes = [1, 2, 3, 4, 5, 6]

edges = [
    (1, 2, 4),		#edge from 1 to 2 with cost of 4
    (1, 3, 2),
    (2, 3, 1),
    (2, 4, 5),
    (3, 4, 8),
    (3, 5, 3),
    (4, 5, 2),
    (4, 6, 6),
    (5, 6, 4)
]
edges.sort(key=lambda x: x[2]) 
print("Edges:", edges)

groups = [[1],[2],[3],[4],[5],[6]]
minEdges = ([])

for node1, node2, cost in edges:
    group1 = None
    group2 = None

    for group in groups:
        if node1 in group:
            group1 = group

        if node2 in group:
            group2 = group
            
    if group1 != group2:
        group1.extend(group2)
        groups.remove(group2)
        minEdges.append([node1,node2])
            
print("MinEdges:", minEdges)
