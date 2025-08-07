import sys


# 실제 제출 시에는 아래 주석을 풀어주세요.
sys.stdin = open('sample_input.txt', 'r')

def dfs(depth, current_result):
    """
    depth: 현재 몇 번째 연산까지 수행했는지 (0부터 N-2까지)
    current_result: 현재 depth까지 계산된 중간 결과값
    """
    global max_result, min_result

    # 종료 조건: 모든 연산자(N-1개)를 다 사용했을 때
    if depth == N - 1:
        # 최종 계산 결과를 최댓값/최솟값과 비교하여 갱신
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    # 4가지 종류의 연산자를 하나씩 시도
    for op_idx in range(4):
        # 만약 해당 연산자가 1개 이상 남아있다면
        if op_counts[op_idx] > 0:

            # 1. 연산자 하나를 사용한다 (개수 1 감소)
            op_counts[op_idx] -= 1

            # 다음 숫자를 가져와서 현재 연산자로 계산
            next_num = numbers[depth + 1]

            if op_idx == 0:  # +
                next_result = current_result + next_num
            elif op_idx == 1:  # -
                next_result = current_result - next_num
            elif op_idx == 2:  # *
                next_result = current_result * next_num
            else:  # /
                next_result = int(current_result / next_num)

            # 2. 계산된 중간 결과를 가지고 다음 단계로 재귀 호출
            dfs(depth + 1, next_result)

            # 3. 중요! 다음 탐색을 위해 사용했던 연산자를 다시 되돌려 놓는다 (백트래킹)
            op_counts[op_idx] += 1


# --- 입력 및 실행 부분 ---
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # op_counts: 연산자 종류별 개수 (+, -, *, /)
    op_counts = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    # 전역 변수인 최댓값, 최솟값 초기화
    max_result = -100000001  # 문제의 제약 조건에 따른 최솟값보다 더 작게
    min_result = 100000001  # 문제의 제약 조건에 따른 최댓값보다 더 크게

    # DFS 시작
    # depth=0 (첫 번째 연산) 부터 시작,
    # 초기 계산값은 첫 번째 숫자 numbers[0]
    dfs(0, numbers[0])

    # 최종 결과 출력
    print(f"#{tc} {max_result - min_result}")