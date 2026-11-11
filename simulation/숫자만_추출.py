# 숫자만 추출
# [핵심] 문자열에서 숫자만 순서대로 이어 붙여 정수로 만들고, 그 수의 약수 개수를 센다.
# [주의] int()로 바꾸면 "0012" 같은 앞자리 0이 자동으로 사라진다.
# [주의] 약수를 1부터 num까지 전부 나눠 보므로 O(num). 제곱근까지만 보고 짝으로 세면 O(√num).
word = input()

def Num(word):
    result = ''
    for char in word:
        if char.isdigit():
            result += char
    return int(result)

def Divisor(num):
    answer = 0
    for i in range(1, num + 1):
        if num % i == 0:
            answer += 1
    return answer

print(Num(word))
print(Divisor(Num(word)))
