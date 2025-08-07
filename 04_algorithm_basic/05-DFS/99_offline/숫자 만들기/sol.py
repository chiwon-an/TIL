import sys
sys.stdin = open('sample_input.txt', 'r')

# 최대 - 최소
'''
결국 숫자의 조합 아님?
모든 경우의 수를 다 따져서 최소 결과 값이랑 최대 결과 값을 받아.
이건 DFS가 맞을듯?

1. 순서대로 연산
2. 
'''

def fine_result(depth):

    global length
    global cal
    global max_result
    global min_result

    # 1. 종료 조건
    if depth == length:

        # !!!!!!!!여기서 숫자 계산 실시!!!!!!!
        temp_result = numbers[0]
        for i in range(N - 1):
            op = p_operators[i]  # i번째 순서의 연산자
            num = numbers[i + 1]  # i+1번째 순서의 숫자

            if op == '+':
                temp_result += num
            elif op == '-':
                temp_result -= num
            elif op == '*':
                temp_result *= num
            elif op == '/':
                # 문제의 조건에 따라 정수 나눗셈 처리
                temp_result = int(temp_result / num)

        # 계산이 끝난 후, 전역 변수인 최댓값/최솟값과 비교하여 갱신
        max_result = max(max_result, temp_result)
        min_result = min(min_result, temp_result)
        return

    # 해당 조건에서 할 수 있는 모든 조건을 추가
    # 2. 해당하는 것의 연산을 실시

    for idx in range(len(cal)):

        if not visited[idx]:

            visited[idx] = True
            p_operators[depth] = cal[idx]

            fine_result(depth+1)

            visited[idx] = False



sep = ['+', '-', '*', '/']

T = int(input())

for tc in range(1,T+1):

    N = int(input())
    max_result = -float('inf')
    min_result = float('inf')

    cal_cnt = list(map(int, input().split()))
    numbers = list(map(int, input().split()))


    temp = []
    cal = []
    length = len(numbers) - 1

    visited = [False] * (N - 1)  # cal 리스트의 연산자를 썼는지 체크
    p_operators = [' '] * (N - 1)  # 하나의 완성된 연산자 순열을 저장할 공간

    for i in range(4):
        temp.append(cal_cnt[i]*sep[i])
        for char in temp[i]:
            cal.append(char)

    # print(cal)
    fine_result(0)
    print(f"#{tc} {max_result - min_result}")