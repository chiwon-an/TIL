import sys
from collections import deque
sys.stdin = open('input (2).txt', 'r')

def get_route():

    queue = deque()
    
    queue.append((s_inx_x, s_idx_y))
    visited = [[0]*16 for _ in range(16)]
    visited[s_inx_x][s_idx_y] = 1

    while queue:
        
        x_idx, y_idx = queue.popleft()

        for k in range(4):
            nx = x_idx + dx[k]
            ny = y_idx + dy[k]

            if miro[nx][ny] == 1: continue

            if visited[nx][ny] == 1: continue

            if miro[nx][ny] == 3:
                return 1
            
            visited[nx][ny] = 1
            queue.append((nx, ny))

    return 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1,11):
    
    # 테케번호 입력
    tc_num = int(input())

    miro = [list(map(int, input())) for i in range(16)]

    # print(miro)

    # 시작좌표 찾기
    iter = 0
    for row in miro:
        for i in range(16):
            if row[i] == 2:
                s_inx_x = iter
                s_idx_y = i
                break
        iter += 1
    
    # print(s_idx_y, s_inx_x)

    print(f'#{tc_num} {get_route()}')