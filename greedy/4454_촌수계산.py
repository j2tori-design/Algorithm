# 4454. 촌수계산
# [핵심] 두 사람 사이의 촌수 = 가족 관계 그래프에서 두 정점을 잇는 최소 간선 수.
# [주의] 모든 간선의 비용이 1이라 힙에서 꺼내는 순서가 BFS와 같다. deque를 쓰는 일반 BFS로도 같은 답이 나오고 더 빠르다.
# [주의] 두 사람이 연결되어 있지 않으면 -1.
import heapq
def Relation(a,b,arr):
    pq = [(0,a)]
    visited = [False]*len(arr)
    visited[a] = True
    while pq:
        dist, curr = heapq.heappop(pq)
        if curr == b:
            return dist
        for i in arr[curr]:
            if not visited[i]:
                visited[i] = True
                heapq.heappush(pq, (dist+1,i))
    return -1

n = int(input())
a,b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
print(Relation(a,b,arr))
