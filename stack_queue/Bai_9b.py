from collections import deque

def bfs_traversal(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for neighbor in graph.get(u, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

sample_graph = {0: [1, 2], 1: [3], 2: [], 3: []}
print("Bài 9:", bfs_traversal(sample_graph, start_node=0))