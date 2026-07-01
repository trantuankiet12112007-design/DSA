def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]
    order = []

    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            order.append(u)
            # Đảo ngược danh sách kề trước khi đưa vào stack để ưu tiên duyệt đỉnh nhỏ trước
            for neighbor in reversed(graph.get(u, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order


sample_graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

print("Bài 13 - Thứ tự duyệt DFS từ đỉnh 0:", dfs_iterative(sample_graph, start_node=0))