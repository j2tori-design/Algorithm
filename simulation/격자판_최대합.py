# 격자판 최대합
# [핵심] 각 행의 합, 각 열의 합, 두 대각선의 합 중 최댓값.
# [주의] 열의 합은 arr[j][i]처럼 행 인덱스를 돌려서 구한다. 반대쪽 대각선의 열 번호는 n-1-i.
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
add = []

def maxSum(n, arr):
    for i in range(n):
        add.append(sum(arr[i]))
        add.append(sum(arr[j][i] for j in range(n)))
    add.append(sum(arr[i][i] for i in range(n)))
    add.append(sum(arr[i][n-1-i] for i in range(n)))
    return max(add)

print(maxSum(N, arr))
