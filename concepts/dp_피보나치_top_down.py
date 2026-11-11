# DP Top-Down 방식: 재귀함수 + 메모이제이션
# [주의] 메모가 없으면 같은 값을 반복 계산해 O(2^n)이고, 메모를 쓰면 O(n)이다. 다만 n이 크면 재귀 깊이 제한에 걸린다.
memo = {}

def fibonacci(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]
