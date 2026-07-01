import heapq

INF = float('inf')


def dijkstra_early_stop(V, adj, source, target):
    dist = [INF] * V
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if u == target:
            return d

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist[target]

V = 6
adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}

shortest_len = dijkstra_early_stop(V, adj, source=0, target=4)
print(f"Bài 6 - Độ dài đường đi ngắn nhất từ 0 đến 4: {shortest_len}")