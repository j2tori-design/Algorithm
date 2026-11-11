# 3212. 위상 정렬
# [핵심] 진입 차수가 0인 정점부터 꺼내고, 꺼낸 정점에서 나가는 간선을 지우면서 새로 0이 된 정점을 넣는다 (Kahn 알고리즘).
# [주의] 큐 대신 최소 힙을 써서, 동시에 꺼낼 수 있는 정점이 여러 개일 때 번호가 작은 것부터 나오게 했다.
import heapq

v,n = map(int,input().split())
graph = [[] for _ in range(v+1)]
degree = [0]*(v+1)

for _ in range(n):
    x,y = map(int, input().split())
    graph[x].append(y)
    degree[y] += 1

# 사이클에 속한 정점은 진입 차수가 끝내 0이 되지 않아 결과에 들어가지 못한다 → 결과 길이가 정점 수보다 작으면 사이클
def has_cycle(v,result):
    if len(result) != v:
        return True
    else:
        return False
    
def Topological(arr):
    heap = []
    for i in range(1,v+1):
        if degree[i]==0:
            heapq.heappush(heap, i)
    
    result = []
    while heap:
        now = heapq.heappop(heap)
        result.append(now)
        
        for next in graph[now]:
            # now를 처리했으므로 now → next 간선을 지운 셈
            degree[next] -= 1
            if degree[next]==0:
                heapq.heappush(heap, next)
        
    return result

answer = Topological(graph)

if has_cycle(v,answer):
    print(-1)
else:
    for i in answer:
        print(i)
