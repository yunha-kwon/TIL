import sys
input = sys.stdin.readline
n = int(input())

end = 0
ans = 0

arr = []

for i in range(0,n):
    a, b = map(int, input().split())
    arr.append([a,b])

arr.sort(key=lambda x: x[1])

for new_start, new_end in arr:
    if end <= new_start:
        ans += 1
        end = new_end

print(ans)