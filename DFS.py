# DFS
V, E = map(int, input().split())
link = list(map(int, input().split()))

def dfs(i, V): # 시작 i, 마지막 V
    visited = [0] * (V+1)
    stack = []
    visited[i] = True
    print(i)

    while True:
        for u in adjl[i]:
            if visited[u] == 0:
                stack.append(i)
                i = u
                visited[i] = 1
                print(i)
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return

#인접리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = link[i*2], link[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

dfs(1, V) # 1에서 V까지 dfs 경로