# 3216. 최단 경로
# [핵심] 다익스트라로 최단 거리를 구하면서 각 정점의 '바로 이전 정점(prev)'을 기록해 두고, 도착지에서 거꾸로 따라가 경로를 복원한다.
# [주의] 정점 이름이 알파벳이라 ord(문자)-ord('A')로 0부터 시작하는 번호로 바꿔 쓴다. 출력할 때는 chr로 되돌린다.
import heapq
INF = 10*1000000

N,M = map(int,input().split())
x,y = input().split()
first = ord(x)-ord('A')
last = ord(y)-ord('A')

way = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = input().split()
    start, end, value = ord(a)-ord('A'), ord(b)-ord('A'), int(c)
    way[start].append((end, value))
    # 양방향 도로이므로 양쪽에 추가
    way[end].append((start,value))

def ShortestPath(way, start, end):
    queue = [(0,start)]
    dist = [INF]*(N+1)
    dist[start] = 0
    prev = [-1]*(N+1)   # 최단 경로에서 바로 이전 정점
    
    while queue:
        value,now = heapq.heappop(queue)
        # 힙에는 같은 정점이 옛 거리로 여러 번 들어 있을 수 있다. 이미 더 짧은 거리로 처리됐다면 버린다
        if dist[now] < value:
            continue
        # 도착지를 꺼낸 순간 그 거리가 최단으로 확정되므로 더 볼 필요가 없다
        if now == end:
            break
        for i,j in way[now]:  # i:도착지, j:시간
            if value + j < dist[i]:
                dist[i] = value + j
                # 거리가 갱신될 때만 prev도 함께 바꿔야 최단 경로와 일치한다
                prev[i] = now
                heapq.heappush(queue, (dist[i], i))
                
    if dist[end] == INF:
        return -1, []
    
    # 도착지에서 prev를 거슬러 올라가 경로 복원
    path = []
    node = end
    while node != -1:
        path.append(chr(node+ord('A')))
        node = prev[node]
    # 도착지 → 출발지 순서로 모았으므로 뒤집는다
    path.reverse()
    
    return dist[end], path
    
total_dist, total_path = ShortestPath(way,first,last)
if total_dist==-1:
    print(-1)
else:
    print(total_dist)
    for node in total_path:
        print(node)
