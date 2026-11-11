# 주사위 게임
# [핵심] 세 눈이 모두 같은 경우 → 두 개만 같은 경우 → 모두 다른 경우 순서로 판별한다.
# [주의] 조건 순서가 중요하다. '두 개가 같다'를 먼저 검사하면 세 개가 같은 경우도 거기서 걸린다.
# [주의] 두 개가 같은 경우는 (0,1), (0,2), (1,2) 세 쌍을 모두 봐야 하고, 어느 쌍이냐에 따라 점수에 쓰는 눈이 달라진다.
# [주의] 변수 이름 list가 내장 list()를 가린다.
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def Dice(N,arr):
    result = []
    for list in arr:
        if list[0] == list[1] == list[2]:
            result.append(10000 + list[0]*1000)
        elif list[0] == list[1] or list[0] == list[2]:
            result.append(1000 + list[0]*100)
        elif list[1] == list[2]:
            result.append(1000 + list[1]*100)
        else:
            result.append(max(list)*100)
    return max(result)

print(Dice(N,arr))
