## BFS 알고리즘
# 큐를 사용하여 연결 노드들을 집어넣고 앞에서부터 pop해서 탐색
# [주의] 방문 표시는 큐에 넣을 때 한다. 꺼낼 때 하면 같은 정점이 큐에 여러 번 들어간다.
# [주의] n과 graph는 문제 입력으로 채워야 한다 (그대로는 실행되지 않는 뼈대).
from collections import deque
n = 00
graph = [[] for _ in range(n)]  # graph 입력
visited = [False] * n  # visited 사용하여 방문여부 체크

def BFS(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for next in graph[now]:
            if not visited[next]:   # 방문안했으면 큐에 추가
                visited[next] = True
                queue.append(next)
BFS(1)
