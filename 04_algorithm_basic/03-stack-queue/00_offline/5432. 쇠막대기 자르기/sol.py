import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1, T+1):
    lst = list(input())

    stack = []
    count = 0
    idx = -1

    for item in lst:
        # 리스트 인덱스
        idx += 1

        # ( 면 일단 넣기
        if item == '(':
            stack.append(item)

        # 닫는 괄호가 나온 경우
        if item == ')':

            # 전 번째 리스트가 여는괄호였다면 넌 레이저다.
            if idx != 0 and lst[idx -1] == '(':
                # stack에 담겨있는 닫는 괄호 가져와
                stack.pop()
                # 지금까지 stack에 담겨 있었던 길이를 count에 더하기
                count += len(stack)

            # 전 번째 리스트가 여는 괄호가 아니였다면, 너는 막대야.
            else:
                stack.pop()
                count += 1
    print(f'#{tc} {count}')