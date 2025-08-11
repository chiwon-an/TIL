import sys
sys.stdin = open('input1.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x,y,direction):
    global path_length

    # 방문처리
    visited[x][y] = True
    path_length += 1

    # 연결된 구조 탐색
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == False:
        dfs(nx, ny, direction)

T = int(input())

for tc in range(1, T+1):
    
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                for k in range(4):
                    visited = [[False]*M for _ in range(N)]
                    path_length = 0
                    dfs(i,j,k)
                    max_length = max(max_length, path_length)

    print(f'#{tc} {max_length}')

