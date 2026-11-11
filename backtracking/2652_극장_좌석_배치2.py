# 2652. 극장 좌석 배치2
# [핵심] n개 좌석에 k명을 서로 이웃하지 않게 앉히는 경우의 수. 좌석마다 '비운다 / 앉힌다'를 고르는 재귀.
# [주의] last는 바로 앞 좌석의 상태(1 = 앉음). 앞자리에 사람이 있으면 이번 좌석에는 앉힐 수 없다.
# [주의] k명을 다 앉힌 순간 바로 1가지로 센다. 남은 좌석은 전부 비우는 한 가지뿐이라 끝까지 내려갈 필요가 없다.
n,k = map(int,input().split())
num = 0

def Theater(last,idx,count):
    global num
    if count==k:
        num += 1
        return
    # 좌석을 다 봤는데 k명을 채우지 못했으면 실패
    elif idx==n and count!=k:
        return
    Theater(0,idx+1,count)
    if last!=1:
        Theater(1,idx+1,count+1)
    return num
print(Theater(-1,0,0))
