from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    res = []
    
    while queue:
        u = queue.popleft()
        res.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return res


g = {1: [2, 3], 2: [4], 3: [4], 4: []}
print(bfs(g, 1))
