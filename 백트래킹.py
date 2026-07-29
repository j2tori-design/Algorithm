'''
# 기본적인 DFS
def DFS():
    visited = True
    for next in graph:
        if not visited:
            DFS(next)
'''
'''
# 백트래킹 기본 구조
def backtracking(depth):
    # 1. 기저 조건 (종료 조건) 확인
    if depth == 목표_깊이:
        # 답을 찾았을 때의 처리 (출력, 저장 등)
        return
    
    # 2. 다음 단계로 나아갈 수 있는 후보군 탐색
    for next_candidate in candidates:
        # 3. 유망성 검사 (조건 확인)
        if is_promising(next_candidate):
            make_choice(next_candidate)       # 선택 진행 (상태 변화)
            
            backtracking(depth + 1)           # 재귀 호출로 다음 단계 탐색
            
            undo_choice(next_candidate)       # 되돌아왔을 때 선택 복구 (상태 원상복구)
'''
'''
# 2652. 극장 좌석 배치2
n,k = map(int,input().split())
num = 0

def Theater(last,idx,count):
    global num
    if count==k:
        num += 1
        return
    elif idx==n and count!=k:
        return
    Theater(0,idx+1,count)
    if last!=1:
        Theater(1,idx+1,count+1)
    return num
print(Theater(-1,0,0))
'''
'''
# 2653. 규칙에 맞는 이진수 만들기
n = int(input())
count = 0
def Binary(last,idx):
    global count
    if idx==n:
        count += 1
        return
    Binary(1,idx+1)
    if last!=0:
        Binary(0,idx+1)
    return count

print(Binary(1,0))
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
'''
# 3009. 부분수열의 합
count = 0
def backtrack(n,s,arr,index,result):
    global count
    if index == n:
        return
    
    if result + arr[index] == s:
        count += 1
    
    backtrack(n,s,arr,index+1,result+arr[index])
    backtrack(n,s,arr,index+1,result)

N,S = map(int,input().split())
arr = list(map(int,input().split()))

backtrack(N,S,arr,0,0)
print(count)
'''

# 4745. 부등호
k = int(input())
sign = list(map(str, input().split()))
num = [0,1,2,3,4,5,6,7,8,9]

def DFS(last,idx,result):
    if idx==k:
        return result
    num.pop(last)
    result += str(last)
    DFS(last+1,idx+1,result)
    if sign[idx]=='>':
        if last-1 not in num:
            DFS(last-1,idx+1,result)
            result += str(last)

print(DFS(0,0,''))