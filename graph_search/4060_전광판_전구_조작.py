# 4060. 전광판 전구 조작
# [핵심] 0으로 이어진 영역의 개수와 1로 이어진 영역의 개수를 각각 세는 연결 요소 문제.
# [주의] BFS 하나에 target(0 또는 1)을 인자로 넘겨 두 경우를 함께 처리한다.
# [주의] 방문 배열을 0용·1용으로 따로 두었지만, 한 칸은 0이나 1 중 하나에만 속하므로 하나로 합쳐도 된다.
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(a,b,m,n,visited, arr, target):
    queue = deque([(a,b)])
    visited[a][b] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]
            if 0<=dx<m and 0<=dy<n:
                # 같은 값(target)인 칸으로만 퍼진다
                if not visited[dx][dy] and arr[dx][dy] == target:
                    visited[dx][dy] = True
                    queue.append((dx,dy))

def Count0(arr,m,n):
    count0 = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0 and not visited0[i][j]:
                BFS(i,j,m,n,visited0,arr,0)
                count0 += 1
    return count0

def Count1(arr,m,n):
    count1 = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and not visited1[i][j]:
                BFS(i,j,m,n,visited1,arr,1)
                count1 += 1
    return count1

M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]
visited0 = [[False]*N for _ in range(M)]
visited1 = [[False]*N for _ in range(M)]

print(Count0(graph,M,N), end=' ')
print(Count1(graph,M,N), end=' ')
