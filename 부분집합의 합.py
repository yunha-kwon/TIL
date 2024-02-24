#백트래킹 기초!!!
def dfs(n, sum, cnt):
    global ans
    # 가지치기: 가장 마지막에 고민하기, 가장 위에 처리하기
    if sum > K:  # 이미 초과
        return

    # 종료조건: n에 관련된 수식
    if n == N:
        if sum == K and cnt == CNT:
            ans += 1
        return

    # 사용하는 경우
    dfs(n + 1, sum + lst[n], cnt + 1)
    # 사용하지 않는 경우
    dfs(n + 1, sum, cnt)


T = int(input())
for tc in range(1, T + 1):
    lst = [i for i in range(1, 13)]
    CNT, K = map(int, input().split())
    N = 12
    ans = 0
    dfs(0, 0, 0)

    print(f'#{tc} {ans}')
