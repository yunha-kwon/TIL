n, m = map(int, input().split())
spd_lst = [0] * 101
t_spd_lst = [0] * 101
limit_lst = []
for _ in range(n):
    limit_lst.append(list(map(int, input().split())))

test_lst = []
for _ in range(m):
    test_lst.append(list(map(int, input().split())))

for i in range(1, n):
    limit_lst[i][0] += limit_lst[i-1][0]
for i in range(1, m):
    test_lst[i][0] += test_lst[i-1][0]

for i in range(n):
    for j in range(1, limit_lst[i][0] + 1):
        if spd_lst[j] == 0:
            spd_lst[j] = limit_lst[i][1]

for i in range(m):
    for j in range(1, test_lst[i][0] + 1):
        if t_spd_lst[j] == 0:
            t_spd_lst[j] = test_lst[i][1]

mx = 0
for i in range(1, 101):
    mx = max(t_spd_lst[i]-spd_lst[i], mx)

print(mx)