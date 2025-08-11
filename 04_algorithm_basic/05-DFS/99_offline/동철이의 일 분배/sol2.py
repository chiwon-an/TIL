import sys
sys.stdin = open('input.txt','r')


def find_max_percent(x, cur_per):

    global max_percent

    # 가지치기
    if cur_per <= max_percent:
        return

    # 종료 조건
    if x == N:
        if cur_per > max_percent:
            max_percent = cur_per
        return
    
    # 해야할 일.
    for y in range(N):

        if visited[y] == False:
            visited[y] = True
            # cur_per *= percents[x][y]
            # 재귀 보내버리기.
            find_max_percent(x+1, cur_per*percents[x][y])
            visited[y] = False

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    percents = [list(map(lambda v: int(v)/100.0, input().split())) for _ in range(N)]

    max_percent = -1
    visited = [False] * N
    cur_per = 1
    find_max_percent(0, cur_per)
    print(f'#{tc} {max_percent * 100:.6f}')