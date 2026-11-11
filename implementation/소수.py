# 소수
# [핵심] 2 ~ N의 각 수를 2부터 자기 자신 전까지 나눠 보며 소수의 개수를 센다.
# [주의] O(N^2)이라 N이 크면 느리다. 에라토스테네스의 체를 쓰면 O(N log log N).
N = int(input())

def isPrime(N):
    result = []
    for i in range(2,N+1):
        count = 0
        for j in range(2,i):
            if i%j==0:
                count += 1
        if count == 0:
            result.append(i)
    return len(result)

print(isPrime(N))
