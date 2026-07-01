def rabin_karp_search(text: str, pattern: str) -> int:
    n, m = len(text), len(pattern)
    if m > n: return -1

    p, mod = 31, 10 ** 9 + 7
    p_pow = 1
    for _ in range(m - 1):
        p_pow = (p_pow * p) % mod
    pattern_hash = 0
    current_window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % mod
        current_window_hash = (current_window_hash * p + ord(text[i])) % mod

    for i in range(n - m + 1):
        if pattern_hash == current_window_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            current_window_hash = (current_window_hash - ord(text[i]) * p_pow) % mod
            current_window_hash = (current_window_hash * p + ord(text[i + m])) % mod
            current_window_hash = (current_window_hash + mod) % mod
    return -1

print("Bài 6 - Vị trí chuỗi 'abc' trong 'zabcd':", rabin_karp_search("zabcd", "abc"))