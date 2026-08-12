## Dynamic Programming의 두가지 유형
# 1. Top-Down 방식: 재귀함수 + 메모이제이션
#    재귀함수를 사용하면서 계산결과 저장
'''
memo = {}

def fibonacci(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]
'''
# 2. Bottom-Up 방식: 반복문 + 테이블
#    반복문을 사용하여 작은 문제부터 차례대로 계산
'''
def fibonacci(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
'''

## 문제풀이
'''
# 3735. LIS
N = int(input())
arr = list(map(int, input().split()))
result = []
dp = [1]*N

def LIS(arr):
    idx = 0
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(LIS(arr))
'''
# 3801. 오르막수
N = int(input())
dp = [1]*N
count = 0

def UpCount(N):
    global count
    for i in range(N-1,-1,-1):
        
    return count
print(UpCount(N))