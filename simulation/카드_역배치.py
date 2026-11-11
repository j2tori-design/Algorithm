# 카드 역배치
# [핵심] 1 ~ 20 카드에서 구간 [ai, bi]를 뒤집는 작업을 10번 반복한다.
# [주의] 양 끝에서 가운데로 오면서 맞바꾼다. 구간의 절반까지만 돌아야 하며, 끝까지 돌면 두 번 바뀌어 원래대로 돌아간다.
# [주의] 카드 번호는 1부터, 리스트 인덱스는 0부터라서 -1 보정이 들어간다. i와 짝이 되는 위치는 bi-(i-ai).
arr = [i for i in range(1,21)]
for _ in range(10):
    ai, bi = map(int, input().split())
    for i in range(ai, (ai+bi)//2 + 1):
        arr[i-1], arr[bi-(i-ai)-1] = arr[bi-(i-ai)-1], arr[i-1]
print(*arr)
