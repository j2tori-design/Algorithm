
'''
# Prim 알고리즘
# 1647.
import heapq
import sys
input = sys.stdin.readline

N,M = map(int, input().split())     # 집(edge), 길(vertex)
route = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    A,B,C = map(int, input().split())
    route[A].append([C,B])
    route[B].append([C,A])

def Prim(x):
    least_num = 0
    max_vertex = 0

    pq=route[x]
    heapq.heapify(pq)
    visited[x] = 1

    while pq:
        w, v = heapq.heappop(pq)
        if visited[v] == 0:
            visited[v] = 1
            least_num += w
            if w > max_vertex:
                max_vertex = w

            for next_w, next_v in route[v]:
                if visited[next_v] == 0:
                    heapq.heappush(pq, [next_w, next_v])

    return least_num - max_vertex

print(Prim(1))
'''
'''
# Kruskal 알고리즘
def initial(n):
    return [i for i in range(n + 1)]

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def equal(parent, p, q):
    return p == q

def merge(parent, p, q):
    parent[q] = p

def kruskal(n, E):
    F = []
    parent = initial(n)
    E.sort()
    for weight, i, j in E:
        p = find(parent, i)
        q = find(parent, j)
        if not equal(parent, p, q):
            merge(parent, p, q)
            F.append((i, j, weight))
        if len(F) == n - 1:
            break
    return F

n = 10
E = [
    (32, 1, 2),(17, 1, 4),(45, 2, 5),
    (18, 3, 4),(5, 3, 7),(10, 4, 5),
    (3, 4, 8),(28, 5, 6),(25, 5, 9),
    (6, 6, 10),(59, 7, 8),(4, 8, 9),
    (12, 9, 10)
]
F = kruskal(n, E)

total = 0
print("MST 간선")
for i, j, weight in F:
    print(f"v{i} - v{j} : {weight}")
    total += weight

print("최소비용:", total)
'''
'''
# 3301. 거스름돈
def Money(n):
    num = 0
    list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in list:
        num += n // i
        n = n % i
    return num

n = int(input())
print(Money(n))
'''
'''
# 2001. 최소대금
def MinCost(op1, op2):
    return (min(op1) + min(op2)) * 1.1

pasta = []
for i in range(3):
    n = int(input())
    pasta.append(n)
juice = []
for i in range(2):
    n = int(input())
    juice.append(n)

print(f"{MinCost(pasta, juice):.1f}")
'''
'''
# 3120. 리모컨
def Remote(diff):
    num = 0
    num += diff // 10
    diff = diff % 10
    if diff == 9 or diff == 8:
        diff -= 10
        num += 1
        while diff != 0:
            diff+=1
            num+=1
        return num
    elif diff == 7 or diff == 6 or diff == 5:
        diff -= 5
        num += 1
        while diff != 0:
            diff-=1
            num+=1
        return num
    elif diff == 4 or diff == 3:
        diff -= 5
        num += 1
        while diff != 0:
            diff += 1
            num += 1
        return num
    else:
        while diff != 0:
            diff-=1
            num+=1
        return num

a,b = map(int, input().split())
diff = abs(a-b)
print(Remote(diff))
'''
'''
# 3215. 최단경로(다익스트라)
import heapq
INF = 10**200
def ShortPath(a,b,arr,result):
    result[a] = 0
    pq = [(0,a)]

    while pq:
        dist, now = heapq.heappop(pq)
        if dist > result[now]:
            continue
        for i in arr[now]:
            if dist + i[1] < result[i[0]]:
                result[i[0]] = dist + i[1]
                heapq.heappush(pq, (dist + i[1], i[0]))

    if result[b] == INF:
        return -1
    else:
        return result[b]

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
length = [INF]*(N+1)
for _ in range(M):
    u, v, w = input().split()
    w = int(w)
    graph[ord(u)-ord('A')].append((ord(v)-ord('A'),w))
    graph[ord(v)-ord('A')].append((ord(u)-ord('A'),w))
a, b = input().split()
print(ShortPath(ord(a)-ord('A'),ord(b)-ord('A'),graph,length))
'''
'''
# 4454. 촌수계산
import heapq
def Relation(a,b,arr):
    pq = [(0,a)]
    visited = [False]*len(arr)
    visited[a] = True
    while pq:
        dist, curr = heapq.heappop(pq)
        if curr == b:
            return dist
        for i in arr[curr]:
            if not visited[i]:
                visited[i] = True
                heapq.heappush(pq, (dist+1,i))
    return -1

n = int(input())
a,b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
print(Relation(a,b,arr))
'''
'''
# 3229. 소들의 코딩 대회
def Fight(arr):
    
N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int, input().split())
    graph[B].append(A)

# 방향그래프로 입력받고 갈수 있는 방법이 하나면 +1
# 초반은 1
'''