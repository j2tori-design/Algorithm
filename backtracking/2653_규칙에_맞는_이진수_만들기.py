# 2653. 규칙에 맞는 이진수 만들기
# [핵심] 길이 n인 이진수 중 0이 연달아 나오지 않는 것의 개수. 자리마다 1 또는 0을 붙여 보는 재귀.
# [주의] 1은 언제나 붙일 수 있고, 0은 바로 앞이 0이 아닐 때만 붙인다.
# [주의] 첫 호출을 last=1로 시작해서 첫 자리에는 0과 1이 모두 올 수 있게 했다.
n = int(input())
count = 0
def Binary(last,idx):
    global count
    if idx==n:
        count += 1
        return
    Binary(1,idx+1)
    if last!=0:
        Binary(0,idx+1)
    return count

print(Binary(1,0))
