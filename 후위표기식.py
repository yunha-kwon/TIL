icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

fx = '(6+5*(2-8)/2)'
postfix = ''

stack = []

for tk in fx:
    if tk == '(' or (tk in '+-*/' and isp[stack[-1]] < icp[tk]):
        stack.append(tk)

    elif tk in '+-*/' and isp[stack[-1]] >= icp[tk]:
        while isp[stack[-1]] >= icp[tk]:
            postfix += stack.pop()

        stack.append(tk)

    elif tk == ')':
        while stack[-1] != '(':
            postfix += stack.pop()

        stack.pop()

    else:
        postfix += tk

print(postfix)