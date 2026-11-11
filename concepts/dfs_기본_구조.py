## DFS 알고리즘
# 스택 혹은 재귀 사용하여 한 방향으로 끝까지 탐색
# 인접 정점 순서에 따라 탐색 순서가 달라질 수 있음
# [주의] 스택 방식은 꺼낼 때 방문 표시를 한다. 같은 정점이 스택에 여러 번 들어갈 수 있어서, 꺼낸 뒤에 방문 여부를 다시 확인한다.
# [주의] n과 graph는 문제 입력으로 채워야 한다 (그대로는 실행되지 않는 뼈대).
n = 00
graph = [[] for _ in range(n)]  # graph 입력
visited = [False] * n  # visited 사용하여 방문여부 체크

def DFS_1(start):   # 재귀 사용 방식
    visited[start] = True
    print(start, end=' ')

    for next in graph[start]:
        if not visited[next]:
            DFS_1(next)
DFS_1(1)

def DFS_2(start):   # 스택 사용 방식
    stack = [start]

    while stack:
        now = stack.pop()   # pop = 해당 노드 방문

        if not visited[now]:
            visited[now] = True
            print(now, end=' ')
            # graph 접근시 역순 삽입
            # 먼저 방문한걸 먼저 탐색하기 위해 reversed 사용
            for next in reversed(graph[now]):
                if not visited[next]:   # 연결된 노드 중 이미 방문한 노드 제외하고 탐색
                    stack.append(next)
DFS_2(1)
