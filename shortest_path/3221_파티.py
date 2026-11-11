# 3221. 파티
# [핵심] 모든 마을 i에 대해 (i → X) + (X → i) 왕복 시간 중 최댓값을 구한다.
# [핵심] X → i 는 X에서 다익스트라 한 번이면 되지만, i → X 는 마을마다 돌리면 N번이 필요하다.
#        간선 방향을 모두 뒤집은 그래프(way2)에서 X를 출발점으로 돌리면 '모든 i → X' 거리를 한 번에 얻는다. → 총 2번
# [주의] 단방향 도로라서 가는 길과 오는 길이 다를 수 있다. 그래서 그래프를 두 개 만든다.
import heapq
INF = 10*100000

N, M, X = map(int, input().split())
way1 = [[] for _ in range(N+1)]
way2 = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, T = map(int, input().split())
    # way1: 원래 방향 (X에서 각 마을로 돌아가는 길)
    way1[start].append((end, T))
    # way2: 방향을 뒤집은 그래프 (각 마을에서 X로 오는 길)
    way2[end].append((start, T))

def ShortestPath(way, start):
    queue = [(0, start)]
    dist = [INF]*(N + 1)
    dist[start] = 0

    while queue:
        value, now = heapq.heappop(queue)
        # 이미 더 짧은 거리로 처리된 정점의 옛 항목은 건너뛴다
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
