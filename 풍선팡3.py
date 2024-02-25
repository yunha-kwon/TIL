T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_lst = []
    for i in range(N):
        for j in range(N):
            sum = arr[i][j]
            for dir in range(4):
                for l in range(1, arr[i][j]+1):
                    nx = i + dx[dir] * l
                    ny = j + dy[dir] * l

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    else:
                        sum += arr[nx][ny]

            sum_lst.append(sum)


    print(f'#{tc}', max(sum_lst) - min(sum_lst))