M, N, K = map(int, input().split())
secret_key = input().split()
my_key = input().split()

flag = False
for i in range(N-M+1):
    if secret_key == my_key[i:i+M]:
        flag = True
        break

if flag:
    print('secret')
else:
    print('normal')