T = int(input())
for tc in range(1, T+1):
    s = list(input())
    stack = []
    stack.append(s[0])

    for i in range(1, len(s)):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])


    print(f'#{tc}', len(stack))