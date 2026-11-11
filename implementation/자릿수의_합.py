# 자릿수의 합
# [핵심] 각 수의 자릿수 합을 구해, 합이 가장 큰 '원래 수'를 출력.
# [주의] index(max(...))는 합이 같은 수가 여러 개면 먼저 나온 것을 고른다.
# [주의] 변수 이름 sum이 내장 함수 sum()을 가린다.
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
