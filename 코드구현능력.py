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
'''
# 정다면체
N,M = map(int, input().split())

def Count(N,M):
    count = [0]*(N+M+1)
    for i in range(1,N+1):
        for j in range(1,M+1):
            count[i+j] += 1
    result = [i for i,j in enumerate(count) if j == max(count)]
    # index 함수는 첫번째 값만 반환...
    return result

print(*Count(N,M))
'''
'''
# 자릿수의 합
N = int(input())
arr = list(map(int, input().split()))

def digit_sum(N, arr):
    result = []
    for x in arr:
        sum = 0
        while x!=0:
            sum += x%10
            x = x//10
        result.append(sum)
    return arr[result.index(max(result))]

print(digit_sum(N, arr))
'''
'''
# 소수
N = int(input())

def isPrime(N):
    result = []
    for i in range(2,N+1):
        count = 0
        for j in range(2,i):
            if i%j==0:
                count += 1
        if count == 0:
            result.append(i)
    return len(result)

print(isPrime(N))
'''
'''
# 뒤집은 소수
N = int(input())
arr = list(map(int, input().split()))

def reverse(x):
    rev = 0
    while x!=0:
        rev = rev * 10 + (x % 10)
        x = x // 10
    return rev

def isPrime(N,arr):
    result = []
    for x in arr:
        count = 0
        rev = reverse(x)
        for i in range(2,rev):
            if rev%i==0:
                count += 1
        if count == 0:
            result.append(rev)
    return result

print(*isPrime(N, arr))
'''
'''
# 주사위 게임
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def Dice(N,arr):
    result = []
    for list in arr:
        if list[0] == list[1] == list[2]:
            result.append(10000 + list[0]*1000)
        elif list[0] == list[1] or list[0] == list[2]:
            result.append(1000 + list[0]*100)
        elif list[1] == list[2]:
            result.append(1000 + list[1]*100)
        else:
            result.append(max(list)*100)
    return max(result)

print(Dice(N,arr))
'''
'''
# 점수계산
N = int(input())
arr = list(map(int, input().split()))

def Score(N,arr):
    result = 0
    count = 0
    for x in arr:
        if x == 1:
            count += 1
            result += count
        else:
            count = 0
    return result

print(Score(N, arr))
'''