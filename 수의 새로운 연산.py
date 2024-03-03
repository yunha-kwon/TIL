dct = {}
r_dct = {}
i, j = 1, 1
for n in range(1, 50000):
    dct[n] = (i, j)
    r_dct[(i, j)] = n
    i, j = i-1, j+1
    if i < 1:
        i, j = j, 1

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())

    pi, pj = dct[p] # 1. p, q값의 좌표로 변환
    qi, qj = dct[q]

    ans = r_dct[(pi+qi, pj+qj)] # 2. 좌표를 값으로 변환
    print(f'#{tc} {ans}')