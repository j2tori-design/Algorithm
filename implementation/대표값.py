# 대표값
# [핵심] 평균을 반올림하고, 평균과의 차이가 가장 작은 값의 번호를 구한다.
# [주의] 파이썬의 round()는 .5를 가까운 짝수로 보낸다 (round(2.5)=2, round(3.5)=4). 일반적인 반올림이 필요하면 int(x + 0.5)를 쓴다.
# [주의] index(min(...))는 차이가 같은 값이 여러 개일 때 맨 앞의 것만 돌려준다. 동점 처리 규칙이 따로 있으면 직접 비교해야 한다.
N = int(input())
arr = list(map(int, input().split()))

def Represent(N, arr):
    avg = round(sum(arr)/N)
    result = [abs(x-avg) for x in arr]
    return avg, result.index(min(result))+1

print(*Represent(N, arr))       # 왜 이상한 인덱스가 반환되는지...
