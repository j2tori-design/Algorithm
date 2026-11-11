# 수들의 합
# [핵심] 연속 구간 arr[i..j]의 합이 M이 되는 경우의 수를 모든 구간에 대해 확인한다.
# [주의] 구간마다 sum()을 다시 계산해서 O(N^3)이다. 원소가 모두 양수라면 투 포인터로 O(N)에 풀 수 있다.
N,M = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(N):
    for j in range(i, N):
        if sum(arr[i:j+1]) == M:
            count += 1
print(count)
