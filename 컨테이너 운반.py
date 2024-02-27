for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    c, t = 0, 0
    total = 0

    while c < n and t < m:
        if trucks[t] >= containers[c]:
            total += containers[c]
            t += 1
        c += 1

    print(f'#{tc} {total}')