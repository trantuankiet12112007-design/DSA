def rabin_karp(pattern, text):
    m, n = len(pattern), len(text)
    if m > n: return -1
    
    p_base = 31
    mod = 10**9 + 7
    p_hash = t_hash = 0
    h = 1
    
    for i in range(m - 1):
        h = (h * p_base) % mod
        
    for i in range(m):
        p_hash = (p_base * p_hash + ord(pattern[i])) % mod
        t_hash = (p_base * t_hash + ord(text[i])) % mod
        
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            t_hash = (p_base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            t_hash = (t_hash + mod) % mod
    return -1

print("Câu 48:", rabin_karp("abc", "zabcd"))
