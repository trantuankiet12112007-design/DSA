def first_uniq_char(s: str) -> int:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1

print("Bài 10 - Vị trí ký tự không lặp của 'leetcode':", first_uniq_char("leetcode"))