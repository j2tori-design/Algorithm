# 3009. 부분수열의 합
# [핵심] 각 원소를 '넣는다 / 넣지 않는다'로 나눠 모든 부분수열(2^N가지)의 합을 확인한다.
# [주의] 합이 S인지는 원소를 넣는 순간에만 확인한다. 끝(index == n)에서 확인하면 아무것도 고르지 않은 경우(합 0)가 S=0일 때 잘못 세어진다.
# [주의] 합이 S가 된 뒤에도 return하지 않는다. 뒤에 음수나 0이 있으면 원소를 더 넣고도 다시 S가 될 수 있다.
count = 0
def backtrack(n,s,arr,index,result):
    global count
    if index == n:
        return
    
    if result + arr[index] == s:
        count += 1
    
    backtrack(n,s,arr,index+1,result+arr[index])
    backtrack(n,s,arr,index+1,result)

N,S = map(int,input().split())
arr = list(map(int,input().split()))

backtrack(N,S,arr,0,0)
print(count)
