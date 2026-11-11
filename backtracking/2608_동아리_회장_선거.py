#2608. 동아리 회장 선거
# [핵심] 길이 n인 문자열을 모두 만드는 완전 탐색을 두 가지 방식으로 구현해 비교했다.
#        backtrack: 리스트 하나를 공유하면서 append → 재귀 → pop 으로 상태를 되돌린다.
#        dfs: 문자열을 인자로 넘긴다. c+"O"가 새 문자열을 만들기 때문에 되돌리는 코드가 필요 없다.
# [주의] 리스트를 공유하는 방식에서 pop을 빼먹으면 이전 선택이 남아 길이가 계속 늘어난다.
n = int(input())
result = []
answer = ""

def backtrack(depth):
    if depth == n:
        print(''.join(result))
        return

    result.append('O')
    backtrack(depth + 1)
    result.pop()

    result.append('X')
    backtrack(depth + 1)
    result.pop()

def dfs(n, c=""):
    if len(c) == n:
        print(c)
        return
    dfs(n,c+"O")
    dfs(n,c+"X")

backtrack(0)
print()
dfs(n,answer)
