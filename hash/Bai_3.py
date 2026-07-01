def count_frequencies(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

print("Bài 3:", count_frequencies(['a', 'b', 'a', 'c', 'a']))