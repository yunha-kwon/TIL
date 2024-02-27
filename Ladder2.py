T = 10
for _ in range(T):
    tc = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]

    mn = float('inf')
    result = 0
    for i in range(N):
        if ladder[0][i] == 1:  #시작지점 찾기
            x, y = 0, i
            cnt = 0
            while x < 99:
                x += 1
                cnt += 1
                if y > 0 and ladder[x][y-1] == 1:
                    while y > 0 and ladder[x][y-1] == 1:
                        y -= 1
                        cnt += 1
                elif y < 99 and ladder[x][y+1] == 1:
                    while y < 99 and ladder[x][y+1] == 1:
                        y += 1
                        cnt += 1

            if mn > cnt:
                mn = cnt
                result = i

    print(f'#{tc} {result}')