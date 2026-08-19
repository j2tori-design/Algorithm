## 다익스트라 알고리즘


# 3221. 파티
import heapq
INF = 10*100000

N, M, X = map(int, input().split())
way1 = [[] for _ in range(N+1)]
way2 = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, T = map(int, input().split())
    way1[start].append((end, T))
    way2[end].append((start, T))

def ShortestPath(way, start):
    queue = [(0, start)]
    dist = [INF]*(N + 1)
    dist[start] = 0

    while queue:
        value, now = heapq.heappop(queue)
        if dist[now] < value:
            continue
        for i,j in way[now]:  # i:도착지, j:시간
            if value + j < dist[i]:
                dist[i] = value + j
                heapq.heappush(queue, (dist[i], i))
                
    return dist

go_home = ShortestPath(way1, X)
go_party = ShortestPath(way2, X)

max_time = 0
for i in range(1, N + 1):
    max_time = max(max_time, go_party[i] + go_home[i])

print(max_time)