# 4019. 동전 줍기
# [핵심] dp[i] = i번째 칸까지 봤을 때 주울 수 있는 최대 금액. 연속한 세 칸을 모두 줍지는 못하는 형태의 점화식이다.
#        i번째 칸에 대해 세 경우 중 최댓값을 고른다.
#        ① i를 줍지 않는다: dp[i-1]
#        ② i만 줍고 i-1은 건너뛴다: dp[i-2] + coin[i]
#        ③ i-1과 i를 연달아 줍고 i-2는 건너뛴다: dp[i-3] + coin[i-1] + coin[i]
# [주의] coin 앞에 0을 붙여 1번부터 쓰게 했다. dp[i-3]을 쓰기 때문에 N이 1, 2일 때는 따로 처리한다.
N = int(input())
coin = [0] + list(map(int, input().split()))

def Coin(coin, N):
    if N == 1:
        return coin[1]
    if N == 2:
        return coin[1] + coin[2]
    
    dp = [0]*(N+1)
    dp[1] = coin[1]
    dp[2] = coin[1] + coin[2]
    
    for i in range(3,N+1):
        dp[i] = max(dp[i-1], dp[i-2] + coin[i], dp[i-3] + coin[i-1] + coin[i])
   
    return dp[N]

print(Coin(coin, N))
