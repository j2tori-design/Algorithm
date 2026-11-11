# 퀵정렬
# [핵심] 가운데 값을 pivot으로 잡고, 왼쪽에서는 pivot 이상인 값을, 오른쪽에서는 pivot 이하인 값을 찾아 서로 바꾼다 (Hoare 분할).
# [주의] 반복이 끝나면 l과 r이 엇갈려 r < l 이 된다. 그래서 다음 구간은 [left, r]과 [l, right].
# [주의] 비교에 등호를 넣지 않는다 (arr[l] < pivot). <= 로 쓰면 pivot과 같은 값에서 멈추지 않아 인덱스가 범위를 벗어날 수 있다.
# [주의] 평균 O(N log N), 최악 O(N^2).
def QuickSort(arr, left, right):
    if left>=right:
        return
    l=left
    r=right
    pivot = arr[(l+r)//2]
    while l<=r:
        while arr[l] < pivot:
            l+=1
        while arr[r] > pivot:
            r-=1
        # 엇갈리지 않았을 때만 교환한다. l == r 일 때도 한 칸씩 움직여야 무한 반복에 빠지지 않는다
        if l<=r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1

    QuickSort(arr, left, r)
    QuickSort(arr, l, right)

arr = [5,2,9,1,7,4]
QuickSort(arr, 0, len(arr)-1)
print(arr)
