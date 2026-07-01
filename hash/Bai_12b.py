import time


def simulate_hash_flooding_impact():
    collision_bucket = []
    n = 5000

    start_time = time.time()
    for i in range(n):
        collision_bucket.append(i)
    duration = time.time() - start_time

    print(f"Bài 12 - Thời gian mô phỏng duyệt chèn va chạm cho {n} phần tử: {duration:.4f} giây.")
    print("Nhận xét: Khi bị flood va chạm, bảng băm bị suy biến tốc độ xử lý về mức O(n) như mảng tuần tuý.")
simulate_hash_flooding_impact()