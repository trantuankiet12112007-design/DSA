from collections import deque

def max_sliding_window(arr, k):
    q = deque()
    res = []
    for i in range(len(arr)):
        if q and q[0] < i - k + 1:
            q.popleft()
        while q and arr[q[-1]] < arr[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(arr[q[0]])
    return res

print("Bài 11:", max_sliding_window([1, 3, -1, -3, 5, 3], 3))