N = int(input())
orders = list(map(int, input().split()))

stack = []
tmp = []

stack.append(1)
for n in range(2, N+1):
    for _ in range(orders[n-1]):
        tmp.append(stack.pop())
    stack.append(n)
    while tmp:
        stack.append(tmp.pop())

print(*stack)