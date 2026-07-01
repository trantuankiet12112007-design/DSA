INF = float('inf')

def print_distances(dist):
    print("--- Kết quả khoảng cách ngắn nhất ---")
    for i in range(len(dist)):
        val = "∞" if dist[i] == INF else dist[i]
        print(f"dist[{i}] = {val}")

dist_g1 = [0, 3, 1, 4, 7, 9]
print_distances(dist_g1)