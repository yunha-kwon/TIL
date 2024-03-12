import sys
input = sys.stdin.readline

N = int(input())
dots = 2
for _ in range(N):
    dots += (dots-1)

print(dots**2)