# memoization(메모이제이션)을 이용한 피보나치
# memo를 위한 배열을 할당하고, 모두 0으로 초기화
# memo[0]을 0으로, memo[1]은 1로 초기화

def fibo(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = 10
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo(n)) #55