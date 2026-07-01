import heapq

INF = float('inf')


def dijkstra_priority_queue(V, adj, source):
    dist = [INF] * V
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

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

dist_heap = dijkstra_priority_queue(V, adj, source=0)
print("Bài 9 (Bản Heap) - Kết quả dist[]:", dist_heap)