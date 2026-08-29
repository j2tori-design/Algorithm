## 다익스트라 알고리즘

# 3216. 최단 경로
import heapq
INF = 10*1000000

N,M = map(int,input().split())
x,y = input().split()
first = ord(x)-ord('A')
last = ord(y)-ord('A')

way = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    start, end, value = ord(a)-ord('A'), ord(b)-ord('A'), int(c)
    way[start].append((end, value))
    way[end].append((start,value))

def ShortestPath(way, start, end):
    queue = [(0,start)]
    dist = [INF]*(N+1)
    dist[start] = 0
    path = []
    
    while queue:
        value,now = heapq.heappop(queue)
        path.append(now+'A')
        if now == end:
            break
        if dist[now] < value:
            continue
        for i,j in way[now]:  # i:도착지, j:시간
            if value + j < dist[i]:
                dist[i] = value + j
                heapq.heappush(queue, (dist[i], i))
                
    if dist[end] == INF:
        return -1, []
    
    return dist[end], path
    
total_dist, total_path = ShortestPath(way,first-'A',last-'A')
if total_dist==-1:
    print(-1)
else:
    print(total_dist)
    for node in total_path:
        print(node)
'''
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
'''