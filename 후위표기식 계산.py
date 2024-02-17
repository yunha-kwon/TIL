postfix = '113+4*5/+'
stack = []

for tk in postfix:
    if tk.isdigit():
        stack.append(tk)
    else:
        b = int(stack.pop())
        a = int(stack.pop())
        if tk == '*':
            stack.append(a*b)
        elif tk == '/':
            stack.append(a/b)
        elif tk == '+':
            stack.append(a+b)
        elif tk == '-':
            stack.append(a-b)

result = stack.pop()
print(result)