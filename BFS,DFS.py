'''
## BFS 알고리즘
# 큐를 사용하여 연결 노드들을 집어넣고 앞에서부터 pop해서 탐색
from collections import deque
n = 00
graph = [[] for _ in range(n)]  # graph 입력
visited = [False] * n  # visited 사용하여 방문여부 체크

def BFS(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for next in graph[now]:
            if not visited[next]:   # 방문안했으면 큐에 추가
                visited[next] = True
                queue.append(next)
BFS(1)
'''
'''
## DFS 알고리즘
# 스택 혹은 재귀 사용하여 한 방향으로 끝까지 탐색
# 인접 정점 순서에 따라 탐색 순서가 달라질 수 있음
n = 00
graph = [[] for _ in range(n)]  # graph 입력
visited = [False] * n  # visited 사용하여 방문여부 체크

def DFS_1(start):   # 재귀 사용 방식
    visited[start] = True
    print(start, end=' ')

    for next in graph[start]:
        if not visited[next]:
            DFS_1(next)
DFS_1(1)

def DFS_2(start):   # 스택 사용 방식
    stack = [start]

    while stack:
        now = stack.pop()   # pop = 해당 노드 방문

        if not visited[now]:
            visited[now] = True
            print(now, end=' ')
            # graph 접근시 역순 삽입
            # 먼저 방문한걸 먼저 탐색하기 위해 reversed 사용
            for next in reversed(graph[now]):
                if not visited[next]:   # 연결된 노드 중 이미 방문한 노드 제외하고 탐색
                    stack.append(next)
DFS_2(1)
'''
'''
# 2605. 캔디팡
from collections import deque

graph = [list(map(int, input().split())) for _ in range(7)]
# list comprehension 사용
visited = [[False]*7 for _ in range(7)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def Game(row, col):
    queue = deque([(row,col)])
    visited[row][col] = True
    count = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            x = a + dr[i]
            y = b + dc[i]

            if 0<=x<7 and 0<=y<7:
                if not visited[x][y] and graph[x][y] == graph[row][col]:
                    visited[x][y] = True
                    queue.append((x,y))
                    count += 1

    return count

def Func():
    area = 0
    for i in range(7):
        for j in range(7):
            if not visited[i][j]:
                if Game(i,j) >= 3:
                    area += 1
    return area

print(Func())
'''
'''
# 3122. 마름모 출력하기
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
                    if abs(x-n) + abs(y-n) < n:
                        visited[x][y] = True
                        queue.append((x,y))

    for i in range(1,2*n):
        for j in range(1,2*n):
            if arr[i][j] == 0:
                print('', end=' ')
            elif arr[i][j] == 1:
                print('*', end='')
        print()

n = int(input())
graph = [[0]*2*n for _ in range(2*n)]
visited = [[False]*2*n for _ in range(2*n)]

Rect(n,graph)
'''
'''
# 2610. 그림판 채우기
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[False]*10 for _ in range(10)]

def Color(arr,a,b):
    if arr[a][b] == '*':
        return arr
    queue = deque([(a,b)])
    visited[a][b] = True
    arr[a][b] = '*'

    while queue:
        da, db = queue.popleft()

        for i in range(4):
            dx = da + dr[i]
            dy = db + dc[i]

            if 0<=dx<10 and 0<=dy<10:
                if arr[dx][dy] == '_':
                    arr[dx][dy] = '*'
                    queue.append((dx,dy))
    return arr

def Draw(arr,a,b):
    Color(arr,a,b)
    for i in range(10):
        for j in range(10):
            print(arr[i][j], end='')
        print()
# 출력시 print(*i)처럼 *을 붙이면 리스트 형식의 출력이 사라짐

arr = [list(input()) for _ in range(10)]
x, y = map(int, input().split())
Draw(arr,y,x)
'''
'''
# 3600. 체스말 이동
from collections import deque

dr = [-2,-1,1,2,-2,-1,1,2]
dc = [-1,-2,-2,-1,1,2,2,1]

def Move(arr,visited,r1,c1,r2,c2):
    queue = deque([(r1,c1)])
    visited[r1][c1] = True

    while queue:
        r,c = queue.popleft()

        if r == r2 and c == c2:
            return count[r][c]

        for i in range(8):
            dx = r + dr[i]
            dy = c + dc[i]

            if 1<=dx<=n and 1<=dy<=n:
                if not visited[dx][dy]:
                    queue.append((dx,dy))
                    visited[dx][dy] = True
                    count[dx][dy] = count[r][c] + 1

n = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
visited = [[False]*(n+1) for _ in range(n+1)]
count = [[0]*(n+1) for _ in range(n+1)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
print(Move(board,visited,r1,c1,r2,c2))
'''
'''
# 4572. 영역 구하기
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
            visited[i][j] = True

Width(graph,M,N)
'''
'''
# 4060. 전광판 전구 조작
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
'''
'''
# 4421. 단지 번호 붙이기
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = []

def BFS(n,a,b,arr,visited):
    queue = deque([(a,b)])
    visited[a][b] = True
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
    result.sort()
    print(num)
    for x in result:
        print(x)

N = int(input())
arr = [list(map(int,input().strip())) for _ in range(N)]    # 입력받을때 strip() 사용하여 공백 제거
visited = [[False]*(N+1) for _ in range(N+1)]

Home(N,arr,visited)
'''
'''
# 4773. 토마토
from collections import deque

dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

def BFS(m,n,h,arr,visited,queue,remain):
    day = 0
    
    while queue and remain > 0:
        size = len(queue)
        
        for _ in range(size):
            x,y,z = queue.popleft()
            
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                
                if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                    if not visited[nx][ny][nz] and arr[nx][ny][nz]==0:
                        visited[nx][ny][nz] = True
                        remain -= 1
                        queue.append((nx,ny,nz))
        if remain >= 0:
            day += 1
    
    return day if remain == 0 else -1

def Tomato(m,n,h,arr,visited):
    queue = deque()
    remain = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    queue.append((i,j,k))
                    visited[i][j][k] = True
                elif arr[i][j][k]==0:
                    remain += 1
    return BFS(m,n,h,arr,visited,queue,remain)

M,N,H = map(int,input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

print(Tomato(M,N,H,arr,visited))
'''

# 4503.
N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
visited = [False]*(N+1)
count = 0
for i in range(M):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

def Birus(x, arr):
    global count
    if not arr[x]:
        return
    visited[x] = True
    
    for next in arr[x]:
        if not visited[next]:
            count += 1
            Birus(next, arr)

Birus(1,arr)
print(count)