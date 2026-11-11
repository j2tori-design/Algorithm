# 4421. 단지 번호 붙이기 (DFS)
# [핵심] 같은 문제를 재귀 DFS로 풀이. 단지 하나를 탐색하는 동안 전역 count에 집 수를 누적한다.
# [주의] 새 단지를 시작할 때마다 count를 0으로 되돌려야 이전 단지의 집 수가 섞이지 않는다.
# [주의] 재귀 깊이가 단지 크기만큼 깊어진다. 격자가 크면 sys.setrecursionlimit 설정이 필요하다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().strip())))
visited = [[False]*N for _ in range(N)]
result = []
count = 0

def dfs(arr,i,j):
    global count
    visited[i][j] = True
    count += 1
    
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0<=x<N and 0<=y<N:
            if not visited[x][y] and arr[x][y]==1:
                dfs(arr,x,y)

def Map(arr):
    global count
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] == 1:
                count = 0
                dfs(arr,i,j)
                result.append(count)
                
    return len(result), result

# 여기서부터 count는 '단지 수'로 다시 쓰인다 (위에서 집 수를 세던 전역 count와 이름이 같다)
count, result = Map(arr)
result.sort()
print(count)
for num in result:
    print(num)
