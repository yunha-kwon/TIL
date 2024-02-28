time = [(5,9), (6,10), (8,11), (1,4), (3,5), (1,6), (5,7), (3,8), (2,13), (12,14)]
time.sort(key=lambda x: x[1], reverse=True)

end_time = time.pop()[1]
ans = 1

while time:
    s, e = time.pop()
    if s >= end_time:
        end_time = e
        ans += 1

print(ans)