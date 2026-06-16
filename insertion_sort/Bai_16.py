def online_insertion_sort(stream):
    a = []
    for x in stream:
        a.append(x)
        j = len(a) - 2
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
        print(a)
    return a

print("Bài 16:")
online_insertion_sort([5, 2, 8, 1])