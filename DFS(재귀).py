def dfs(i):  # 시작 i, 마지막 V
    visited[i] = 1  # 방문 표시
    print(i)  # 출력
    # i에 인접하고 방문 안 한 w가 있으면,
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접 리스트
adjl = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)  # 방향이 없는 경우

visited = [0] * (V + 1)  # visited, stack 생성 및 초기화
dfs(1)