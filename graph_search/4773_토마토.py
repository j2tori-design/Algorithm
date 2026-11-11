# 4773. 토마토
# [핵심] 익은 토마토 전부를 처음부터 큐에 넣고 동시에 퍼뜨리는 다중 시작점 BFS (3차원, 6방향).
# [주의] 하루 단위로 세기 위해, 그날 시작할 때 큐에 있던 개수(size)만큼만 꺼낸 뒤 day를 올린다.
# [주의] 안 익은 토마토 수(remain)를 세어 두면, 끝난 뒤 격자를 다시 훑지 않아도 전부 익었는지(0) 남았는지(-1) 알 수 있다.
from collections import deque

dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

def BFS(m,n,h,arr,visited,queue,remain):
    day = 0
    
    # remain이 0이면 더 볼 필요가 없다. 처음부터 0이면 day=0이 그대로 반환된다
    while queue and remain > 0:
        size = len(queue)
        
        for _ in range(size):
            x,y,z = queue.popleft()
            
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                
                # 배열이 arr[높이][세로][가로] 순서라서 x는 H, y는 N, z는 M으로 범위를 검사한다
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
# 입력은 층(H)마다 N줄씩 들어오므로 바깥이 H, 안쪽이 N
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

print(Tomato(M,N,H,arr,visited))
