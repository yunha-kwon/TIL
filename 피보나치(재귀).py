# 재귀함수를 이용한 피보나치
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10)) #55