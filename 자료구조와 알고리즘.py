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

# k번째 큰 수
N, K = map(int, input().split())
arr = list(map(int, input().split()))

def K_big(n,k,arr):
    