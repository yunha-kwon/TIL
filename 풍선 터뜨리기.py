from collections import deque

N = int(input())
q = deque(enumerate(map(int, input().split())))
#deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])

stack = []
while q:
    idx, num = q.popleft()
    stack.append(idx + 1)

    if num > 0:
        q.rotate(-(num-1))

    else:
        q.rotate(-num)

print(stack)