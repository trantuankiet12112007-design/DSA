def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if t in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if t == '+': stack.append(a + b)
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            elif t == '/': stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[0]

print(eval_rpn(["3", "4", "+", "2", "*"]))
