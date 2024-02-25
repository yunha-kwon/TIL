def calc(a_lst, b_lst):
    a_sum = b_sum = 0
    for i in range(M):
        for j in range(M):
            a_sum += arr[a_lst[i]][a_lst[j]]
            b_sum += arr[b_lst[i]][b_lst[j]]
    return abs(a_sum - b_sum)

def dfs(n, a_lst, b_lst):
    global ans
    if n == N:
        if len(a_lst) == len(b_lst):
            ans = min(ans, calc(a_lst, b_lst))
        return
    dfs(n+1, a_lst+[n], b_lst)
    dfs(n+1, a_lst, b_lst+[n])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N // 2
ans = 100 * M * M
dfs(0, [], [])
print(ans)