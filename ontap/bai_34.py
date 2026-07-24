def remove_duplicates_O_n(a):
    seen = set()
    res = []
    for x in a:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res

print(remove_duplicates_O_n([3, 1, 3, 2, 1]))
