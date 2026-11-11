# k번째 수
# [핵심] 배열의 s번째 ~ e번째 구간을 잘라 정렬한 뒤 k번째 값을 출력.
# [주의] 문제의 번호는 1부터, 인덱스는 0부터라서 arr[i-1], result[k-1]로 접근한다. 슬라이싱으로 쓰면 arr[s-1:e].
T = int(input())
for idx in range(T):
    N,s,e,k = map(int, input().split())
    result = []
    arr = list(map(int, input().split()))
    for i in range(s, e+1):
        result.append(arr[i-1])
    result.sort()
    print(f'#{idx+1} {result[k-1]}')
