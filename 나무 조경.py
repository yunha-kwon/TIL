import sys
input = sys.stdin.readline

def dfs(m, sm):
    global ans
    if m == d: #기저조건
        ans = max(ans, sm)
        return

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                continue
            for dir in range(2):
                nx = i + dx[dir]
                ny = j + dy[dir]

                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    visited[i][j] = 1
                    visited[nx][ny] = 1
                    dfs(m+1, sm + trees[i][j] + trees[nx][ny])
                    visited[i][j] = 0
                    visited[nx][ny] = 0

n = int(input())
trees = [list(map(int, input().split())) for _ in range(n)]

ans = 0

dx = [0,1]
dy = [1,0]

if n == 2:
    d = 2
else:
    d = 4

visited = [[0] * n for _ in range(n)]

dfs(0,0)
print(ans)