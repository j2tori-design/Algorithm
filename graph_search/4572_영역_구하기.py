# 4572. 영역 구하기
# [핵심] 직사각형들로 덮이지 않은 칸이 몇 개의 영역으로 나뉘는지, 각 영역의 넓이를 BFS로 구한다.
# [주의] 직사각형은 꼭짓점 좌표로 주어진다. 칸으로 바꾸면 x는 xl ~ xr-1, y는 yl ~ yr-1 이고, range의 끝이 제외되는 것과 그대로 맞는다.
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
result = []

def BFS(a,b,m,n):
    queue = deque([(a,b)])
    visited[a][b] = True
    count = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]
            if 0<=dx<m and 0<=dy<n:
                # 덮인 칸은 입력 단계에서 이미 visited=True로 막아 두었으므로 여기서 graph 값을 다시 확인하지 않아도 된다
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    queue.append((dx,dy))
                    count += 1
    return count

def Width(arr,m,n):
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0 and not visited[i][j]:
                area = BFS(i,j,m,n)
                result.append(area)
    print(len(result))
    result.sort()
    print(*result)      # 언패킹하여 출력

M,N,K = map(int,input().split())
graph = [[0]*(N+1) for _ in range(M+1)]
visited = [[False]*(N+1) for _ in range(M+1)]
for _ in range(K):
    xl,yl,xr,yr = map(int, input().split())
    for i in range(yl,yr):
        for j in range(xl,xr):
            graph[i][j] = 1
            # 덮인 칸을 미리 방문 처리 → BFS가 들어가지 못한다
            visited[i][j] = True

Width(graph,M,N)
