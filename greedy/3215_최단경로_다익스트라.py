# 3215. 최단경로(다익스트라)
# [핵심] 우선순위 큐 다익스트라. 힙에서 꺼낸 거리가 이미 기록된 거리보다 크면 옛 항목이므로 건너뛴다.
# [주의] 힙에는 (거리, 정점) 순서로 넣어야 거리가 작은 것부터 나온다.
# [주의] 정점 이름이 알파벳이라 ord(문자)-ord('A')로 번호로 바꿔 쓴다.
import heapq
INF = 10**200
def ShortPath(a,b,arr,result):
    result[a] = 0
    pq = [(0,a)]

    while pq:
        dist, now = heapq.heappop(pq)
        if dist > result[now]:
            continue
        for i in arr[now]:
            if dist + i[1] < result[i[0]]:
                result[i[0]] = dist + i[1]
                heapq.heappush(pq, (dist + i[1], i[0]))

    if result[b] == INF:
        return -1
    else:
        return result[b]

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
length = [INF]*(N+1)
for _ in range(M):
    u, v, w = input().split()
    w = int(w)
    graph[ord(u)-ord('A')].append((ord(v)-ord('A'),w))
    graph[ord(v)-ord('A')].append((ord(u)-ord('A'),w))
a, b = input().split()
print(ShortPath(ord(a)-ord('A'),ord(b)-ord('A'),graph,length))
