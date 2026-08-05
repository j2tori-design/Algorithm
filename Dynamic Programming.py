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

def UpCount(N):
    for i in range(N):
        for j in range(i):
            dp[i] = (dp[i] + dp[j])
    return sum(dp) % 10007

print(UpCount(N))