def insertion_sort(arr):    # 삽입정렬
    n = len(arr)
    for i in range(1,n):
        x = arr[i]      # 현재 삽입할 값 저장
        j = i-1         # 정렬된 구간의 마지막 인덱스
        while j>=0 and arr[j]>x:    # x보다 큰 값들은 한칸씩 뒤로 이동
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
    return arr

def selection_sort(arr):     # 선택정렬
    n = len(arr)
    for i in range(n-1):    # 마지막 원소 전까지 수행
        smallest = i        # 현재 위치를 최솟값 위치라 가정
        for j in range(i+1,n):
            if arr[j] < arr[smallest]:  # 현재 최소값보다 작다면
                smallest = j    # 현재 인덱스를 smallest로 update
        arr[i], arr[smallest] = arr[smallest], arr[i]   # 최소값과 현재 위치 교환
    return arr

arr = [5,1,2,3,7,29,38]

print(f"삽입정렬 결과 : {insertion_sort(arr)}")
print(f"선택정렬 결과 : {selection_sort(arr)}")