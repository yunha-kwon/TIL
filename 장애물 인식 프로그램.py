dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            dfs(nx, ny)

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
lst = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            lst.append(cnt)

print(len(lst))
lst.sort()
for x in lst:
    print(x)