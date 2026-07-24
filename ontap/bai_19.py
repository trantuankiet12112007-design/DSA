import heapq

def min_path_grid(grid):
    m, n = len(grid), len(grid[0])
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    while pq:
        d, r, c = heapq.heappop(pq)
        if d > dist[r][c]:
            continue
        if r == m - 1 and c == n - 1:
            return d
            
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                if dist[r][c] + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + grid[nr][nc]
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))
    return dist[m-1][n-1]

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(min_path_grid(grid))
