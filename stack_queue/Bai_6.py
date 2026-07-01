def is_balanced(brackets: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in brackets:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return len(stack) == 0


print("Bài 6 (case 1):", is_balanced("([]{})"))
print("Bài 6 (case 2):", is_balanced("([)]"))