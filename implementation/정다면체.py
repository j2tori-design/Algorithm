# 정다면체
# [핵심] 두 주사위 눈의 합이 나오는 횟수를 모두 세어, 가장 자주 나오는 합을 전부 출력.
# [주의] 가장 자주 나오는 합이 여러 개일 수 있어 index()가 아니라 enumerate로 전부 모은다.
# [주의] 리스트 컴프리헨션 안에서 max(count)를 매번 다시 계산한다. 미리 변수에 담아 두면 한 번만 계산한다.
N,M = map(int, input().split())

def Count(N,M):
    count = [0]*(N+M+1)
    for i in range(1,N+1):
        for j in range(1,M+1):
            count[i+j] += 1
    result = [i for i,j in enumerate(count) if j == max(count)]
    # index 함수는 첫번째 값만 반환...
    return result

print(*Count(N,M))
