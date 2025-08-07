import sys
sys.stdin = open('input.txt', 'r')

def find_min_top(idx, current_sum):
    global cnt
    cnt += 1
    global ans
    global result

    # 백트래킹
    if current_sum > ans:
        return

    # 종료 조건
    if idx == N:
        if current_sum >= B:
            ans = min(ans, current_sum)

        return


    # 현재 idx에서 할 수 있는 모든 선택지를 시도해야지

    # 이번 idx를 한 번 더해볼까?

    find_min_top(idx+1, current_sum+height[idx])


    # 이번엔 안 더할게~
    find_min_top(idx+1, current_sum)


T = int(input())

for tc in range(1, T+1):
    cnt = 0
    result = []
    N, B = map(int, input().split())

    height = list(map(int, input().split()))

    ans = float('inf')

    current_sum = 0

    find_min_top(0,0)
    print(f'#{tc} {ans-B}')
    print(cnt)


