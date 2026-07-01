def count_nodes_within_radius(dist, D):
    valid_nodes = [i for i in range(len(dist)) if dist[i] <= D]
    return len(valid_nodes), valid_nodes

dist_g1 = [0, 3, 1, 4, 7, 9]
D_value = 3

count, nodes = count_nodes_within_radius(dist_g1, D_value)
print(f"Bài 8 - Với D = {D_value}: Có {count} đỉnh thoả mãn. Danh sách đỉnh: {nodes}")
