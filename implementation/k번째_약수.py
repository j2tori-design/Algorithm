# k번째 약수
# [핵심] 1부터 차례로 나눠 보며 약수를 세다가 k번째가 나오는 순간 반환.
# [주의] 약수가 k개보다 적으면 -1.
N, K = map(int, input().split())

def F(n,k):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count += 1
            if count == k:
                return i
    return -1

print(F(N, K))
