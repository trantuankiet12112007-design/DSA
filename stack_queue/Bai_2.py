def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)

    reversed_s = ""
    while stack:
        reversed_s += stack.pop()
    return reversed_s

print("Bài 2:", reverse_string("abc"))