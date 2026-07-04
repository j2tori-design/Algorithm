'''
# 합병정렬
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
'''
'''
# 퀵정렬
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
        if l<=r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1

    QuickSort(arr, left, r)
    QuickSort(arr, l, right)

arr = [5,2,9,1,7,4]
QuickSort(arr, 0, len(arr)-1)
print(arr)
'''