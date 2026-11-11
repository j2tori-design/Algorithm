# 3120. 리모컨
# [핵심] 두 값의 차이를 ±10, ±5, ±1 버튼으로 맞추는 최소 누름 횟수. 10 단위는 몫으로 먼저 처리하고, 남은 0 ~ 9는 경우를 나눈다.
# [주의] 나머지가 8·9면 10을 한 번 더 누르고 되돌아오는 편이 빠르다 (9 → +10, -1 로 2번). 4도 5를 누르고 되돌아온다 (+5, -1 로 2번).
# [주의] 큰 버튼부터 쓰는 단순 그리디로는 이런 '넘겼다가 되돌아오기'를 놓친다.
def Remote(diff):
    num = 0
    num += diff // 10
    diff = diff % 10
    if diff == 9 or diff == 8:
        diff -= 10
        num += 1
        while diff != 0:
            diff+=1
            num+=1
        return num
    elif diff == 7 or diff == 6 or diff == 5:
        diff -= 5
        num += 1
        while diff != 0:
            diff-=1
            num+=1
        return num
    elif diff == 4 or diff == 3:
        diff -= 5
        num += 1
        while diff != 0:
            diff += 1
            num += 1
        return num
    else:
        while diff != 0:
            diff-=1
            num+=1
        return num

a,b = map(int, input().split())
diff = abs(a-b)
print(Remote(diff))
