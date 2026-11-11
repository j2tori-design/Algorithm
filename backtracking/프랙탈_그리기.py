# 프랙탈 그리기
# [핵심] 한 변이 n인 삼각형을 그리면서, 각 꼭짓점에서 절반 크기의 삼각형을 먼저 그리는 재귀 (시에르핀스키 삼각형 형태).
# [주의] n이 5 이하가 되면 멈춘다. 종료 조건이 없으면 무한 재귀에 빠진다.
from turtle import *
penup()
setpos((-200,-200))
pendown()
speed(0)

def fract(n):
    if n>5:
        for _ in range(3):
            fract(n//2)
            fd(n)
            left(120)
fract(400)
done()
