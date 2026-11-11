# 4421. 단지 번호 붙이기
# [핵심] 1로 이어진 집 묶음(단지)의 개수와 각 단지의 집 수를 BFS로 구해 오름차순으로 출력.
# [주의] 입력이 "0110100"처럼 공백 없이 붙어 있어 split()을 쓸 수 없다. 문자열을 한 글자씩 int로 바꾼다.
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = []

def BFS(n,a,b,arr,visited):
    queue = deque([(a,b)])
    visited[a][b] = True
    # 시작한 집도 포함
    size = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and arr[nx][ny]==1:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    size += 1
    result.append(size)

def Home(n,arr,visited):
    num = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] == 1:
                BFS(n,i,j,arr,visited)
                num += 1
    # 단지별 집 수는 오름차순으로 출력
    result.sort()
    print(num)
    for x in result:
        print(x)

N = int(input())
arr = [list(map(int,input().strip())) for _ in range(N)]    # 입력받을때 strip() 사용하여 공백 제거
visited = [[False]*(N+1) for _ in range(N+1)]

Home(N,arr,visited)
