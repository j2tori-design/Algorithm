# 4745. 부등호
# [핵심] 0 ~ 9를 한 번씩만 써서 부등호 k개를 만족하는 k+1자리 수를 모두 만들고, 최댓값과 최솟값을 출력.
# [주의] 숫자를 0부터 차례로 시도하므로 answer에는 작은 수부터 쌓인다. 정렬 없이 answer[0]이 최소, answer[-1]이 최대.
# [주의] 첫 자리가 0일 수 있어서 정수가 아니라 문자열로 이어 붙인다. int로 바꾸면 앞의 0이 사라진다.
k = int(input())
sign = list(map(str, input().split()))
visited = [False]*10
answer = []

def DFS(idx,current):
    if idx==k+1:
        answer.append(current)
        return

    for i in range(10):
        if not visited[i]:
            # 첫 자리(idx == 0)는 조건 없이 통과. 그 뒤로는 직전 숫자 current[-1]과 부등호 sign[idx-1]로 비교
            if idx==0 or (sign[idx-1]=='<' and int(current[-1])<i) or (sign[idx-1]=='>' and int(current[-1])>i):
                visited[i] = True
                DFS(idx+1,current+str(i))
                visited[i] = False

DFS(0,"")
print(answer[-1])
print(answer[0])
