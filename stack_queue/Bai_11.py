def next_greater_element(arr):
    n = len(arr)
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            res[idx] = arr[i]
        stack.append(i)
    return res


print("Bài 11:", next_greater_element([2, 1, 3]))