from collections import deque

def max_sliding_window(a, k):
    q = deque()
    res = []
    for i, x in enumerate(a):
        if q and q[0] <= i - k:
            q.popleft()
        while q and a[q[-1]] < x:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(a[q[0]])
    return res

print(max_sliding_window([1, 3, -1, -3, 5, 3], 3))
