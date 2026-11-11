# DP Bottom-Up 방식: 반복문 + 테이블
# [주의] n이 0일 때 dp[1]에 접근하면 범위를 벗어나므로 n >= 1 조건을 둔다.
def fibonacci(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
