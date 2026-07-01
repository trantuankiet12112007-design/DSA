INF = float('inf')
def dijkstra_v2(V, adj, source):
    dist = [INF] * V
    visited = [False] * V
    dist[source] = 0

    for _ in range(V):
        u = -1
        min_d = INF
        for i in range(V):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist

V = 6
adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}

dist_result = dijkstra_v2(V, adj, source=0)
print("Bài 3 - Kết quả dist[]:", dist_result)