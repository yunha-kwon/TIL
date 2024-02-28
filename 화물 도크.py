T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort(key = lambda x: x[1], reverse=True)

    ans = 1
    end = time.pop()[1]

    while time:
        s, e = time.pop()
        if end <= s:
            end = e
            ans += 1

    print(f'#{tc} {ans}')