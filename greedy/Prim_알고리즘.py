# Prim 알고리즘
# 1647.
# [핵심] 최소 신장 트리를 Prim으로 구한 뒤 그중 가장 비싼 간선 하나를 빼서 둘로 나눈다 → (트리 전체 비용) - (트리에서 가장 큰 간선).
# [주의] 힙에는 [가중치, 정점] 순서로 넣는다. 꺼냈을 때 이미 방문한 정점이면 버린다 (옛 항목).
# [주의] max_vertex는 이름과 달리 '가장 큰 간선 가중치'를 담는다.
# [주의] 입력이 많아 input을 sys.stdin.readline으로 바꿔 썼다.
import heapq
import sys
input = sys.stdin.readline

N,M = map(int, input().split())     # N: 집(정점) 수, M: 길(간선) 수
route = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    A,B,C = map(int, input().split())
    route[A].append([C,B])
    route[B].append([C,A])

def Prim(x):
    least_num = 0
    max_vertex = 0

    # 시작 정점의 간선 목록을 그대로 힙으로 쓴다 (route[x] 자체가 바뀐다)
    pq=route[x]
    heapq.heapify(pq)
    visited[x] = 1

    while pq:
        w, v = heapq.heappop(pq)
        if visited[v] == 0:
            visited[v] = 1
            least_num += w
            if w > max_vertex:
                max_vertex = w

            for next_w, next_v in route[v]:
                if visited[next_v] == 0:
                    heapq.heappush(pq, [next_w, next_v])

    return least_num - max_vertex

print(Prim(1))
