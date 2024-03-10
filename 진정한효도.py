farm = [list(map(int, input().split())) for _ in range(3)]

ans = 9

#행 탐색
for i in range(3):
    x, y, z = farm[i]
    if x == y == z:
        print(0)
        exit() #같은 게 있다면 열 탐색까지 가지 않고 아예 종료해버려야 되므로 break가 아닌 exit()
    else:
        mid = sum(farm[i]) - max(farm[i]) - min(farm[i])
        tmp = (max(farm[i]) - mid) + (mid - min(farm[i]))
        ans = min(tmp, ans)

#열 탐색
for i in range(3):
    lst = []
    for j in range(3):
        lst.append(farm[j][i])
    if lst[0] == lst[1] == lst[2]:
        print(0)
        exit()
    else:
        mid = sum(lst) - max(lst) - min(lst)
        tmp = (max(lst) - mid) + (mid - min(lst))
        ans = min(tmp, ans)

print(ans)