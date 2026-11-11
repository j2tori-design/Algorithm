# 2001. 최소대금
# [핵심] 파스타 3종 중 최솟값 + 주스 2종 중 최솟값에 10%를 더한 금액.
# [주의] 소수 첫째 자리까지 출력하기 위해 f-string의 :.1f 서식을 썼다.
def MinCost(op1, op2):
    return (min(op1) + min(op2)) * 1.1

pasta = []
for i in range(3):
    n = int(input())
    pasta.append(n)
juice = []
for i in range(2):
    n = int(input())
    juice.append(n)

print(f"{MinCost(pasta, juice):.1f}")
