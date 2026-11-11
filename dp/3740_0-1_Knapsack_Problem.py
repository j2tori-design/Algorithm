# 3740. 0/1 Knapsack Problem
# - Greedy 알고리즘으로는 해결할 수 없는 문제
# - Dynamic Programming을 이용하여 해결
# [핵심] dp[j] = 용량 j 이하로 담을 수 있는 최대 가치. 물건을 하나씩 보면서 갱신하는 1차원 DP.
# [주의] j는 큰 쪽에서 작은 쪽으로 돌아야 한다. 작은 쪽부터 돌면 방금 이 물건을 넣어 갱신한 dp[j-w]를 다시 써서 같은 물건을 여러 번 넣게 된다.
N,W = map(int,input().split())
# dp[W] : 용량이 W일 때 담을 수 있는 최대 가치
dp = [0]*(W+1)

for _ in range(N):
    w,v = map(int,input().split())

    for j in range(W, w-1, -1):    # 역순 탐색
        dp[j] = max(dp[j], dp[j-w] + v)
        
print(dp[W])
