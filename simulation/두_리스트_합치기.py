# 두 리스트 합치기
# [핵심] 두 리스트를 이어 붙인 뒤 정렬한다. O((N+M) log(N+M)).
# [주의] 두 리스트가 이미 정렬되어 있다면 포인터 두 개로 앞에서부터 비교하며 합치는 방법(O(N+M))도 있다. 합병정렬의 합치기 단계와 같다.
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

result = arr1 + arr2
result.sort()
print(*result)
