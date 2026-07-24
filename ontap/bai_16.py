import heapq

def dijkstra_path(n, graph, s, t):
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if u == t:
            break
            
        if d > dist[u]:
            continue
            
        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
                
    if dist[t] == float('inf'):
        return []
        
    path = []
    curr = t
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
        
    path.reverse()
    return path

g = {
    0: [(2, 1)], 
    2: [(1, 2)], 
    1: [(3, 1)], 
    3: [(4, 2)]
}

print(dijkstra_path(5, g, 0, 4))  
