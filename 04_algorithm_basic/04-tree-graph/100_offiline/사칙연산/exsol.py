import sys
sys.stdin = open('input.txt','r')

def cal(idx):
    # 리프 노드(숫자)면 그대로 반환
    if isinstance(tree[idx], int):
        return tree[idx]

    # 연산자라면 왼쪽/오른쪽 값 먼저 구하고 계산
    left_val = cal(left[idx])
    right_val = cal(right[idx])

    if tree[idx] == '+':
        return left_val + right_val
    elif tree[idx] == '-':
        return left_val - right_val
    elif tree[idx] == '*':
        return left_val * right_val
    elif tree[idx] == '/':
        return left_val / right_val

# 테스트 케이스 10개
for tc in range(1, 11):
    N = int(input())

    tree = [None] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        line = input().split()

        idx = int(line[0])
        value = line[1]

        if value.isdigit():  # 숫자이면
            tree[idx] = int(value)
        else:  # 연산자이면
            tree[idx] = value
            left[idx] = int(line[2])
            right[idx] = int(line[3])

    result = cal(1)
    print(f'#{tc} {int(result)}')