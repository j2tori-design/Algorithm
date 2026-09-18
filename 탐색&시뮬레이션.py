'''
# 회문 문자열 검사
N = int(input())

def isAnswer(word):
    for i in range(len(word)//2):
        if word[i] == word[len(word)-1-i]:
            continue
        else:
            return "NO"
    return "Yes"

for i in range(N):
    word = input()
    print(f"#{i+1} : {isAnswer(word)}")
'''  
'''
# 숫자만 추출
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
'''

# 