# Kruskal 알고리즘
# [핵심] 간선을 가중치 오름차순으로 보면서, 두 끝점이 서로 다른 집합일 때만 채택한다 (사이클 방지). 집합 관리는 Union-Find.
# [주의] 간선을 (가중치, 정점, 정점) 순서의 튜플로 두어 sort()만으로 가중치순 정렬이 된다.
# [주의] 정점이 n개면 최소 신장 트리의 간선은 n-1개. 다 모이면 바로 멈춘다.
def initial(n):
    return [i for i in range(n + 1)]

def find(parent, i):
    if parent[i] != i:
        # 경로 압축: 찾는 길에 만난 정점을 루트에 바로 연결해 다음 탐색을 빠르게 한다
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
        # 정점 번호가 아니라 각 정점의 '루트'끼리 비교하고 합쳐야 한다
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
