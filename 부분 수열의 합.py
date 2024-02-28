def dfs(idx, current_sm):
    global result

    if current_sm == k:
        result += 1
        return

    if idx == n:
        if current_sm == k:
            result += 1
        return

    dfs(idx+1, current_sm + arr[idx])
    dfs(idx+1, current_sm)

    return

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(n):
        dfs(i+1, arr[i])

    print(f'#{tc} {result}')