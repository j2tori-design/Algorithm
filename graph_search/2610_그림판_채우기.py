# 2610. 그림판 채우기
# [핵심] 시작 칸에서 상하좌우로 이어진 빈 칸('_')을 BFS로 모두 '*'로 바꾸는 flood fill.
# [주의] 입력은 x(열), y(행) 순서라서 배열에는 arr[y][x]로 접근해야 한다. 맨 아래에서 Draw(arr,y,x)로 순서를 바꿔 넘기는 이유.
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[False]*10 for _ in range(10)]

def Color(arr,a,b):
    # 시작 칸이 이미 칠해져 있으면 아무것도 하지 않는다
    if arr[a][b] == '*':
        return arr
    queue = deque([(a,b)])
    visited[a][b] = True
    arr[a][b] = '*'

    while queue:
        da, db = queue.popleft()

        for i in range(4):
            dx = da + dr[i]
            dy = db + dc[i]

            if 0<=dx<10 and 0<=dy<10:
                # 칠하는 것 자체가 방문 표시 역할을 한다. '_'였던 칸만 큐에 넣고 바로 '*'로 바꾸므로 visited 없이도 중복 방문이 없다
                if arr[dx][dy] == '_':
                    arr[dx][dy] = '*'
                    queue.append((dx,dy))
    return arr

def Draw(arr,a,b):
    Color(arr,a,b)
    for i in range(10):
        for j in range(10):
            print(arr[i][j], end='')
        print()
# 출력시 print(*i)처럼 *을 붙이면 리스트 형식의 출력이 사라짐

arr = [list(input()) for _ in range(10)]
x, y = map(int, input().split())
Draw(arr,y,x)
