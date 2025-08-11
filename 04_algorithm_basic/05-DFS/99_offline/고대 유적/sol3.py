import sys
sys.stdin = open('input1.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
 
def dfs(x, y, direction):
    global path_length
 
    # 방문 처리
    visited[x][y] = True
    path_length += 1
 
    # 연결된 구조물 탐색
    nx = x + dx[direction] # 이동할 x 좌표
    ny = y + dy[direction] # 이동할 y 좌표
    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1 and not visited[nx][ny]: # 이동 가능 여부 체크
        dfs(nx, ny, direction)
 
 
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N: 행, M: 열
    grid = [list(map(int, input().split())) for _ in range(N)]
 
    max_length = 0
 
    # 탐색 지점
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                for d in range(4):
                    visited = [[False] * M for _ in range(N)] # 방문 여부
                    path_length = 0 # 경로 길이
                    dfs(i, j, d) # 한 방향으로 탐색
                    max_length = max(max_length, path_length) # 최대 경로 길이
 
    print(f'#{test_case} {max_length}')