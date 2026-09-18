'''
# 회문 문자열 검사
N = int(input())

def isAnswer(word):
    for i in range(len(word)//2):
        if word[i] == word[len(word)-1-i]:
            continue
        else:
            return "NO"
    return "Yes"

for i in range(N):
    word = input()
    print(f"#{i+1} : {isAnswer(word)}")
'''  
'''
# 숫자만 추출
word = input()

def Num(word):
    result = ''
    for char in word:
        if char.isdigit():
            result += char
    return int(result)

def Divisor(num):
    answer = 0
    for i in range(1, num + 1):
        if num % i == 0:
            answer += 1
    return answer

print(Num(word))
print(Divisor(Num(word)))
'''
'''
# 카드 역배치
arr = [i for i in range(1,21)]
for _ in range(10):
    ai, bi = map(int, input().split())
    for i in range(ai, (ai+bi)//2 + 1):
        arr[i-1], arr[bi-(i-ai)-1] = arr[bi-(i-ai)-1], arr[i-1]
print(*arr)
'''
'''
# 두 리스트 합치기
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

result = arr1 + arr2
result.sort()
print(*result)
'''
'''
# 수들의 합
N,M = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(N):
    for j in range(i, N):
        if sum(arr[i:j+1]) == M:
            count += 1
print(count)
'''
'''
# 격자판 최대합
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
add = []

def maxSum(n, arr):
    for i in range(n):
        add.append(sum(arr[i]))
        add.append(sum(arr[j][i] for j in range(n)))
    add.append(sum(arr[i][i] for i in range(n)))
    add.append(sum(arr[i][n-1-i] for i in range(n)))
    return max(add)

print(maxSum(N, arr))
'''
'''
# 사과나무(다이아몬드)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mid = N//2
result = 0

for i in range(-mid, mid+1):
    limit = mid - abs(i)
    for j in range(-limit, limit+1):
        result += arr[mid+i][mid+j]
print(result)
'''
'''
# 곳감(모래시계) - 오답 출력됩니다ㅜ
from copy import deepcopy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
newArr = deepcopy(arr)

for _ in range(M):
    x, y, z = map(int, input().split())
    if y == 0:
        for i in range(N):
            newArr[x-1][i] = arr[x-1][(z+i)%N]
    else:
        for i in range(N):
            newArr[x-1][(z+i)%N] = arr[x-1][z]

result = 0
mid = N//2
for i in range(-mid, mid+1):
    for j in range(-abs(i), abs(i)+1):
        result += newArr[mid+i][mid+j]
        
print(result)
'''

