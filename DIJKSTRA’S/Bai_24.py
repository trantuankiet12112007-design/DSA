import heapq

INF = float('inf')
def manhattan_heuristic(r, c, target_r, target_c):
    return abs(target_r - r) + abs(target_c - c)


def a_star_on_grid(grid):
    R = len(grid)
    C = len(grid[0])
    target_r, target_c = R - 1, C - 1


    g_score = [[INF] * C for _ in range(R)]
    g_score[0][0] = grid[0][0]

    start_f = g_score[0][0] + manhattan_heuristic(0, 0, target_r, target_c)
    pq = [(start_f, g_score[0][0], 0, 0)]

    nodes_explored = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        f, g, r, c = heapq.heappop(pq)
        nodes_explored += 1

        if r == target_r and c == target_c:
            return g, nodes_explored

        if g > g_score[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                new_g = g_score[r][c] + grid[nr][nc]
                if new_g < g_score[nr][nc]:
                    g_score[nr][nc] = new_g
                    new_f = new_g + manhattan_heuristic(nr, nc, target_r, target_c)
                    heapq.heappush(pq, (new_f, new_g, nr, nc))

    return g_score[target_r][target_c], nodes_explored

cost_grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

cost, nodes = a_star_on_grid(cost_grid)
print(f"Bài 24 (Bản A*) - Tổng chi phí: {cost} | Số lượng ô đã duyệt qua: {nodes}")