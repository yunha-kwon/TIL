w, n = map(int, input().split())
jewerly = [list(map(int, input().split())) for _ in range(n)]
jewerly.sort(key=lambda x: x[1], reverse=True) #귀금속 가격을 기준으로 오름차순 정렬

total = 0
for m, p in jewerly:
    if m >= w:
        total += w * p
        break
    else:
        total += m * p
        w -= m

print(total)