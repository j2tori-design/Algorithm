# 사과나무(다이아몬드)
# [핵심] N×N 격자(N은 홀수) 가운데의 마름모 영역 합. 가운데 행에서 |i|칸 떨어진 행은 좌우로 (mid - |i|)칸까지만 포함된다.
# [주의] 행·열을 가운데(mid) 기준의 상대 위치(-mid ~ mid)로 돌리면 범위 계산이 단순해진다.
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mid = N//2
result = 0

for i in range(-mid, mid+1):
    limit = mid - abs(i)
    for j in range(-limit, limit+1):
        result += arr[mid+i][mid+j]
print(result)
