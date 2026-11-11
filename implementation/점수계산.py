# 점수계산
# [핵심] 연속으로 맞힌 횟수(count)가 그 문제의 점수가 된다. 틀리면 count를 0으로 되돌린다.
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
