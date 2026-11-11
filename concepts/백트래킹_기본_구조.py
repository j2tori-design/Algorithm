# 백트래킹 기본 구조
# [주의] 선택 → 재귀 → 되돌리기가 한 묶음이다. 되돌리기를 빼먹으면 다른 가지에 이전 선택이 남는다.
def backtracking(depth):
    # 1. 기저 조건 (종료 조건) 확인
    if depth == 목표_깊이:
        # 답을 찾았을 때의 처리 (출력, 저장 등)
        return
    
    # 2. 다음 단계로 나아갈 수 있는 후보군 탐색
    for next_candidate in candidates:
        # 3. 유망성 검사 (조건 확인)
        if is_promising(next_candidate):
            make_choice(next_candidate)       # 선택 진행 (상태 변화)
            
            backtracking(depth + 1)           # 재귀 호출로 다음 단계 탐색
            
            undo_choice(next_candidate)       # 되돌아왔을 때 선택 복구 (상태 원상복구)
