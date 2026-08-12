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
'''
# 3801. 오르막수
N = int(input())
dp = [[0]*10 for _ in range(N+1)]
count = 0

def UpCount(N):
    for j in range(10):
        dp[1][j] = 1

    for k in range(2, N+1):
        for i in range(10):
            for j in range(i+1):
                dp[k][i] += dp[k-1][j]
                dp[k][i] %= 10007

    count = sum(dp[N]) % 10007
    return count
    
print(UpCount(N))

1 1 1 1 1~9
1 1 1 2 2~9 
1 1 1 3 3~9
...
1 1 1 9 9~9 : 9+8+7+6+5+...+1

1 1 2 2~9 : 8+7+6+5+...+1
...
1 1 9 9~9 : 1
-> 9*1+8*2+7*3+6*4+5*5+4*6+3*7+2*8+1*9

1 2 2~9 : 8*1+7*2+6*3+5*4+4*5+3*6+2*7+1*8
...
1 7 7~9 : 3+2*2+1*3
1 8 8~9 : 2+1*2
1 9 9~9 : 1
-> 8*1+7*(1+2)+6*(1+2+3)+5*(1+2+3+4)+4*(1+2+3+4+5)+3*(1+2+3+4+5+6)+2*(1+2+3+4+5+6+7)+1*(1+2+3+4+5+6+7+8)
=> 9*1+8*(1+2)+7*(1+2+3)+6*(1+2+3+4)+5*(1+2+3+4+5)+4*(1+2+3+4+5+6)+3*(1+2+3+4+5+6+7)+2*(1+2+3+4+5+6+7+8)+1*(1+2+3+4+5+6+7+8)

2 2~9 : 8*1+7*(1+2)+6*(1+2+3)+5*(1+2+3+4)+4*(1+2+3+4+5)+3*(1+2+3+4+5+6)+2*(1+2+3+4+5+6+7)+1*(1+2+3+4+5+6+7+8)
...
7 7~9 : 3*1+2*(1+2)+1*(1+2+3)
8 8~9 : 2+1*(1+2)
9 9~9 : 1
'''

# 3740. 0/1 Knapsack Problem
N,W = map(int,input().split())
object = []
for _ in range(N):
    w,v = map(int,input().split())
    object.append((w,v))

def Knapsack(object, W):
    