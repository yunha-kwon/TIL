N = int(input())
for i in range(1, N+1):
    flag = False
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        flag = True

    for j in str(i):
        if '3' in j or '6' in j or '9' in j:
            print('-', end='')
        elif not flag:
            print(j, end='')
    print('', end = ' ')