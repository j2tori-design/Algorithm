# 3735. LIS
# [핵심] dp[i] = arr[i]를 마지막 원소로 하는 가장 긴 증가 부분수열의 길이. 앞쪽 j 중 arr[j] < arr[i]인 것의 dp[j]+1 최댓값.
# [주의] 답은 dp[N-1]이 아니라 max(dp). 가장 긴 수열이 마지막 원소에서 끝난다는 보장이 없다.
# [주의] 이중 반복문이라 O(N^2). N이 크면 이분 탐색(bisect)을 쓰는 O(N log N) 풀이가 필요하다.
N = int(input())
arr = list(map(int, input().split()))
result = []
# 원소 하나만으로도 길이 1
dp = [1]*N

def LIS(arr):
    idx = 0
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(LIS(arr))
