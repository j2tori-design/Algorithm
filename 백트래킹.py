'''
# 기본적인 DFS
def DFS():
    visited = True
    for next in graph:
        if not visited:
            DFS(next)
'''
'''
# 3520. 체커 도전
N = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
result = []

def DFS(arr,start):    # start = (i,j)
    list = [start[1]]
    if start[0] > N:
        return
    visited[start[1]] = True

    for k in range(1,N+1):
        if not visited[k] and abs(start[0]-start[1]) != abs(start[0]+1-k):
            list.append(k)
            DFS(arr,(start[0]+1,k))

def Sol(arr):
    for i in range(1,N+1):
        result.append(DFS(arr,(1,i)))
'''
'''
#2608. 동아리 회장 선거
n = int(input())
result = []
answer = ""

def backtrack(depth):
    if depth == n:
        print(''.join(result))
        return

    result.append('0')
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
'''
'''
# 프랙탈 그리기
from turtle import *
penup()
setpos((-200,-200))
pendown()
speed(0)

def fract(n):
    if n>5:
        for _ in range(3):
            fract(n//2)
            fd(n)
            left(120)
fract(400)
done()
'''
# 3501. RGB거리
def RGB(i):
    if
    RGB(i-1)
    RGB(i+1)
N = int(input())
cost = [[] for _ in range(N)]
for i in range(N):
    cost[i].append(list(map(int, input().split())))