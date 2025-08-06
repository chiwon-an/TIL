import sys
from collections import deque
sys.stdin = open('input (1).txt','r')


#     상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]




def get_miro_move_time(miro):

    queue = deque()
    queue.append((st_idx_x, st_idx_y))

    visited = [[0] * 100 for _ in range(100)]
    visited[st_idx_x][st_idx_y] = 1

    while queue:
        row, col = queue.popleft()

        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            # 범위를 벗어났으면 조사 못함
            if nx < 0 or nx >= 100 or ny < 0 or ny >= 100: continue

            # 이미 방문한 경우
            if visited[nx][ny]: continue

            # 길이 아닌 경우 continue
            if miro[nx][ny] == 1: continue

            # 도착 지점인 경우
            if miro[nx][ny] == 3:
                return 1

            visited[nx][ny] = 1
            queue.append((nx, ny))

    return 0


for tc in range(1, 11):
    tc = int(input())
    miro = [list(map(int, input())) for _ in range(100)]
    # print(miro)
    # print(f'{tc} {result}')

    iter = 0

    for row in miro:
        if 2 in row:
            st_idx_y = row.index(2)
            st_idx_x = iter
        iter += 1

    # print(st_idx_y, st_idx_x)
    result = get_miro_move_time(miro)

    print(f'#{tc} {result}')

    # find_




    #
    #     if 3 in row:
    #         end_idx_y = row.index(3)