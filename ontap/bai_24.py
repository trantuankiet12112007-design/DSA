def next_greater_element(a):
    n = len(a)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and a[i] > a[stack[-1]]:
            idx = stack.pop()
            res[idx] = a[i]
        stack.append(i)
    return res

print(next_greater_element([2, 1, 3]))
