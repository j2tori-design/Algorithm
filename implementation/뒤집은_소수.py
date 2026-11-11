# 뒤집은 소수
# [핵심] 수를 뒤집은 뒤 그 수가 소수이면 출력. 뒤집기는 % 10으로 끝자리를 떼어 rev*10 뒤에 붙이는 방식.
# [주의] 숫자로 뒤집으면 910 → 19처럼 앞자리 0이 자연스럽게 사라진다.
# [주의] 뒤집은 수가 1이면 나눠 볼 수가 없어 count가 0으로 남는다. 1은 소수가 아니므로 rev > 1 조건으로 걸러 낸다.
N = int(input())
arr = list(map(int, input().split()))

def reverse(x):
    rev = 0
    while x!=0:
        rev = rev * 10 + (x % 10)
        x = x // 10
    return rev

def isPrime(N,arr):
    result = []
    for x in arr:
        count = 0
        rev = reverse(x)
        for i in range(2,rev):
            if rev%i==0:
                count += 1
        if count == 0 and rev > 1:
            result.append(rev)
    return result

print(*isPrime(N, arr))
