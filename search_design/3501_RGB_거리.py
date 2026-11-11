# 3501. RGB 거리
# [핵심] sum[i][c] = i번째 집을 색 c로 칠했을 때 1 ~ i번 집까지의 최소 비용. 이웃한 집은 같은 색을 쓸 수 없으므로 직전 집의 '다른 두 색' 중 작은 값을 더한다.
# [주의] sum은 1번부터, cost는 0번부터 쓰기 때문에 cost[i-1]로 접근한다.
# [주의] sum이라는 이름이 내장 함수 sum()을 가린다. 이 파일 안에서는 sum()을 쓸 수 없게 된다.
def RGB_dist(N, cost, sum):
    for i in range(1,N+1):
        sum[i][0] = cost[i - 1][0] + min(sum[i - 1][1], sum[i - 1][2])
        sum[i][1] = cost[i - 1][1] + min(sum[i - 1][0], sum[i - 1][2])
        sum[i][2] = cost[i - 1][2] + min(sum[i - 1][0], sum[i - 1][1])
    return min(sum[N])

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
sum = [[0] * 3 for _ in range(N+1)]

print(RGB_dist(N,cost,sum))
