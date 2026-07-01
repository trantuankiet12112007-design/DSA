import heapq

INF = float('inf')
def dijkstra_with_parent(V, adj, source):
    dist = [INF] * V
    parent = [-1] * V
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    return parent


def reconstruct_path(parent, source, target):
    if parent[target] == -1 and source != target:
        return "Không có đường đi"

    path = []
    v = target
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()
    return " -> ".join(map(str, path))



V = 6
adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}

parent_array = dijkstra_with_parent(V, adj, source=0)
path_string = reconstruct_path(parent_array, source=0, target=4)
print(f"Bài 7 - Đường đi ngắn nhất từ 0 đến 4: {path_string}")
