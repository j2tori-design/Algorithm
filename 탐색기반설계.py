'''
# 3501. RGB 거리
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
'''

# 4880. 서울에서 경산까지
def MaxCost(n,k,arr):
    for i in range(n):
        wt, wc, bt, bc = arr[i]
    """
    time = 0
    cost = 0
    for i in range(n):
        time += arr[i][0]
        cost += arr[i][1]
    if time <= k:
        return cost

    target = time - k
    diff = []
    for i in range(n):
        diffTime = arr[i][0] - arr[i][2]
        diffCost = arr[i][1] - arr[i][3]
        diff.append((diffCost/diffTime, diffTime, diffCost))

    diff.sort(key=lambda x:x[0])
    for i in range(n):
        dff, d_time, d_cost = diff[i]
        if d_time >= target:
            cost -= d_cost
            break
        else:
            cost -= d_cost
            target -= d_time
    return cost
    """
N, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
print(MaxCost(N,K,array))