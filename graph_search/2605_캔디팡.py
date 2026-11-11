# 2605. 캔디팡
# [핵심] 7x7 격자에서 같은 색으로 이어진 칸 묶음(연결 요소)의 크기를 BFS로 세고, 크기가 3 이상인 묶음의 개수를 구한다.
# [주의] 방문 표시는 큐에서 꺼낼 때가 아니라 넣을 때 한다. 꺼낼 때 표시하면 같은 칸이 큐에 여러 번 들어가 count가 부풀려진다.
from collections import deque

graph = [list(map(int, input().split())) for _ in range(7)]
# list comprehension 사용
visited = [[False]*7 for _ in range(7)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def Game(row, col):
    queue = deque([(row,col)])
    visited[row][col] = True
    # 시작 칸도 묶음에 포함되므로 1부터 센다
    count = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            x = a + dr[i]
            y = b + dc[i]

            if 0<=x<7 and 0<=y<7:
                # 색 비교 기준은 직전 칸 (a,b)가 아니라 시작 칸 (row,col). 같은 색만 이어 가므로 결과는 같지만 기준이 고정되어 읽기 쉽다
                if not visited[x][y] and graph[x][y] == graph[row][col]:
                    visited[x][y] = True
                    queue.append((x,y))
                    count += 1

    return count

def Func():
    area = 0
    for i in range(7):
        for j in range(7):
            # 이미 어떤 묶음에 속한 칸은 건너뛰어야 같은 묶음을 두 번 세지 않는다
            if not visited[i][j]:
                if Game(i,j) >= 3:
                    area += 1
    return area

print(Func())
