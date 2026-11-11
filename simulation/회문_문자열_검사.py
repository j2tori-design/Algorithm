# 회문 문자열 검사
# [핵심] 앞에서 i번째 글자와 뒤에서 i번째 글자를 절반까지만 비교한다.
# [주의] 대소문자를 구분해서 비교한다. 대소문자를 무시해야 하는 문제라면 먼저 lower()나 upper()로 통일해야 한다.
N = int(input())

def isAnswer(word):
    for i in range(len(word)//2):
        if word[i] == word[len(word)-1-i]:
            continue
        else:
            return "NO"
    return "YES"

for i in range(N):
    word = input()
    print(f"#{i+1} : {isAnswer(word)}")
