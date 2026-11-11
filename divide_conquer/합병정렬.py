# 합병정렬
# [핵심] 반으로 나눠 각각 정렬한 뒤, 정렬된 두 구간을 앞에서부터 비교하며 합친다. 입력과 무관하게 O(N log N).
# [주의] arr[i] <= arr[j] 에 등호를 넣어야 같은 값일 때 왼쪽 것이 먼저 들어가 원래 순서가 유지된다 (안정 정렬).
# [주의] 합칠 때 임시 리스트(newArr)가 필요해 추가 메모리 O(N)을 쓴다.
def MergeSort(arr, left, right):
    if left>=right:
        return
    mid = (left+right)//2
    MergeSort(arr, left, mid)
    MergeSort(arr, mid+1, right)
    Merge(arr, left, mid, right)

def Merge(arr, left, mid, right):
    # arr 배열 전체를 받은뒤 인덱스로 값 비교
    newArr = []
    i = left
    j = mid+1
    # 인덱스로 비교
    while i<=mid and j<=right:
        if arr[i] <= arr[j]:
            newArr.append(arr[i])
            i+=1
        else:
            newArr.append(arr[j])
            j+=1
    # 남은 값 복사
    while i <= mid:
        newArr.append(arr[i])
        i += 1
    while j <= right:
        newArr.append(arr[j])
        j += 1
    # 원래 배열에 복사
    for k in range(len(newArr)):
        arr[left + k] = newArr[k]

arr = [5,2,9,1,7,4]
MergeSort(arr, 0, len(arr)-1)
print(arr)
