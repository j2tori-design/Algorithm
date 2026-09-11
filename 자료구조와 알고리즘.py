## 코드구현능력 기르기
'''
# k번째 약수
N, K = map(int, input().split())

def F(n,k):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count += 1
            if count == k:
                return i
    return -1

print(F(N, K))
'''
'''
# k번째 수
T = int(input())
for idx in range(T):
    N,s,e,k = map(int, input().split())
    result = []
    arr = list(map(int, input().split()))
    for i in range(s, e+1):
        result.append(arr[i-1])
    result.sort()
    print(f'#{idx+1} {result[k-1]}')
'''
'''
# k번째 큰 수
# 어떠한 기준으로 최대값을 구하는지
N, K = map(int, input().split())
arr = list(map(int, input().split()))

def K_big(n,k,arr):
'''
'''
# 대표값
N = int(input())
arr = list(map(int, input().split()))

def Represent(N, arr):
    avg = round(sum(arr)/N)
    result = [abs(x-avg) for x in arr]
    return avg, result.index(min(result))+1

print(*Represent(N, arr))       # 왜 이상한 인덱스가 반환되는지...
'''