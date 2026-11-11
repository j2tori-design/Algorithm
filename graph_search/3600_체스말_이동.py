# 3600. 체스말 이동
# [핵심] 나이트의 8방향 이동으로 목표 칸까지 가는 최소 이동 횟수. 모든 이동의 비용이 1이므로 BFS에서 처음 도착한 순간이 최단이다.
# [주의] 이동 횟수는 count[dx][dy] = count[r][c] + 1 로 칸마다 저장한다. 변수 하나로 세면 같은 단계의 다른 칸들과 섞인다.
# [주의] 도달할 수 없는 경우는 처리하지 않았다 (함수가 None을 반환한다).
from collections import deque

# 나이트 이동 8가지: (±2, ±1), (±1, ±2)
dr = [-2,-1,1,2,-2,-1,1,2]
dc = [-1,-2,-2,-1,1,2,2,1]

def Move(arr,visited,r1,c1,r2,c2):
    queue = deque([(r1,c1)])
    visited[r1][c1] = True

    while queue:
        r,c = queue.popleft()

        # 큐에서 꺼낸 시점에 목표인지 확인한다. 시작 칸과 목표 칸이 같으면 0이 반환된다
        if r == r2 and c == c2:
            return count[r][c]

        for i in range(8):
            dx = r + dr[i]
            dy = c + dc[i]

            # 판은 1 ~ n (1부터 시작)
            if 1<=dx<=n and 1<=dy<=n:
                if not visited[dx][dy]:
                    queue.append((dx,dy))
                    visited[dx][dy] = True
                    count[dx][dy] = count[r][c] + 1

n = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
visited = [[False]*(n+1) for _ in range(n+1)]
count = [[0]*(n+1) for _ in range(n+1)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
print(Move(board,visited,r1,c1,r2,c2))
