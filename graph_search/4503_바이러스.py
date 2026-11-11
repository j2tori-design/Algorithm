# 4503. 바이러스
# [핵심] 1번과 직접·간접으로 연결된 컴퓨터 수 = 1번이 속한 연결 요소의 크기 - 1. 재귀 DFS로 센다.
# [주의] 양방향 연결이므로 인접 리스트의 양쪽에 모두 추가한다.
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
    # 연결이 하나도 없는 정점이면 바로 종료
    if not arr[x]:
        return
    visited[x] = True
    
    for next in arr[x]:
        if not visited[next]:
            # 새로 방문하는 정점마다 +1. 1번 자신은 세지 않으므로 1번을 뺀 수만 남는다
            count += 1
            Birus(next, arr)

Birus(1,arr)
print(count)
