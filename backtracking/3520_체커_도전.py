# 3520. 체커 도전
# [핵심] N-Queens. 한 행에 하나씩 놓으므로 행은 겹치지 않고, 열과 두 방향의 대각선만 검사하면 된다.
# [주의] 같은 ↘ 대각선 위의 칸은 (행 - 열)이 같고, 같은 ↙ 대각선 위의 칸은 (행 + 열)이 같다. 이 값을 기록해 두면 대각선 충돌을 바로 알 수 있다.
# [주의] 재귀에서 돌아오면 열·대각선 기록을 반드시 되돌린다.
# [주의] 대각선 기록이 리스트라서 in 검사가 O(N)이다. 집합(set)이나 bool 배열로 바꾸면 O(1).
N = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)   # 열 방문 여부
result = []
row_col1 = []
row_col2 = []

def DFS(start,answer):
    if start == N+1:
        result.append(answer)
        return

    for i in range(1,N+1):
        if not visited[i]:
            if (start-i not in row_col1) and (start+i not in row_col2):
                visited[i] = True
                row_col1.append(start-i)
                row_col2.append(start+i)
                
                # answer+[i]는 새 리스트를 만들므로 answer는 따로 되돌릴 필요가 없다
                DFS(start+1,answer+[i])
                
                visited[i] = False
                row_col1.pop()
                row_col2.pop()

DFS(1, [])
# 열을 1부터 차례로 시도했기 때문에 result는 이미 사전순이다. 앞의 3개만 출력
for i in range(3):
    print(*result[i])
print(len(result))
