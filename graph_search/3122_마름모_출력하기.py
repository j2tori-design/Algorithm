# 3122. 마름모 출력하기
# [핵심] 중심 (n,n)에서 BFS로 퍼지면서 맨해튼 거리 |x-n|+|y-n| < n 인 칸만 채우면 마름모가 된다.
# [주의] 격자를 1 ~ 2n-1 범위(1부터 시작)로 쓰기 위해 크기를 2n으로 잡았다. 0번 행·열은 쓰지 않는다.
from collections import deque

dr = [-1,1,0,0]
dl = [0,0,-1,1]

def Rect(n,arr):
    queue = deque([(n, n)])
    visited[n][n] = True

    while queue:
        i, j = queue.popleft()
        arr[i][j] = 1

        for k in range(4):
            x = i + dr[k]
            y = j + dl[k]

            if 1<=x<2*n and 1<=y<2*n:
                if not visited[x][y]:
                    # 중심에서의 맨해튼 거리가 n 미만인 칸만 마름모 안쪽
                    if abs(x-n) + abs(y-n) < n:
                        visited[x][y] = True
                        queue.append((x,y))

    for i in range(1,2*n):
        for j in range(1,2*n):
            if arr[i][j] == 0:
                # 빈 칸은 공백 한 글자로 출력해 별의 위치를 맞춘다
                print('', end=' ')
            elif arr[i][j] == 1:
                print('*', end='')
        print()

n = int(input())
# [0]*2*n 은 ([0]*2)*n 으로 계산되어 길이 2n짜리 리스트가 된다
graph = [[0]*2*n for _ in range(2*n)]
visited = [[False]*2*n for _ in range(2*n)]

Rect(n,graph)
