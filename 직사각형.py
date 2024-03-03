for _ in range(4):
    si1, sj1, ei1, ej1, si2, sj2, ei2, ej2 = map(int, input().split())

    if si1 > ei2 or ei1 < si2 or sj1 > ej2 or ej1 < sj2: #공통부분 x
        ans = 'd'

    elif ej1 == sj2 or sj1 == ej2:
        if ei1 == si2 or si1 == ei2: #세로 일치 & 가로 일치
            ans = 'c'
        else: #세로 일치 & 가로 불일치
            ans = 'b'

    elif ei1 == si2 or si1 == ei2: #세로 불일치 & 가로 일치
        ans = 'b'

    else:
        ans = 'a'

    print(ans)