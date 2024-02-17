#괄호문제
stack = []
b = '({[]})()(()){{}}'

for i in b:
    if i == '(' or i == '{' or i == '[':
        stack.append(i)
    elif stack and i == ')' and stack[-1] == '(':
        stack.pop()
    elif stack and i == '}' and stack[-1] == '{':
        stack.pop()
    elif stack and i == ']' and stack[-1] == '[':
        stack.pop()
    elif i == ')' or i == '}' and i == ']':
        stack.append(i)

    if stack:
        answer = 'false'
    else:
        answer = 'true'

print(answer) #true