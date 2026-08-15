# 3221. 파티
N, M, X = map(int, input().split())
way = [[]for _ in range(N+1)]
time = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, T = map(int, input().split())
    way[start].append((end, T))

def LongestTime(N, X):
    for i in range(1, N+1):
        for j in way[i]:
            end, T = j
            while end != X:
                
            time[i].append(T)