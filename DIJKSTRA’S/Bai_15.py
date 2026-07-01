import heapq

INF = float('inf')
def dijkstra_on_grid(grid):
    R = len(grid)
    C = len(grid[0])

    dist = [[INF] * C for _ in range(R)]
    dist[0][0] = grid[0][0]

    pq = [(grid[0][0], 0, 0)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        d, r, c = heapq.heappop(pq)


        if r == R - 1 and c == C - 1:
            return d

        if d > dist[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:

                if dist[r][c] + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + grid[nr][nc]
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))

    return dist[R - 1][C - 1]



cost_grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

min_cost = dijkstra_on_grid(cost_grid)
print(f"Bài 15 - Tổng chi phí nhỏ nhất trên lưới tới đích: {min_cost}")