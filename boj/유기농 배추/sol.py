import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

T = int(input())

def bfs(sx, sy):
        
    queue = deque([(sx, sy)])
    visited[sx][sy] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            
            nx = x +dx[k]
            ny = y +dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    bfs(nx, ny)


for tc in range(1, T+1):

    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]

    cabbages = []

    for i in range(K):

        y, x = map(int, input().split())
        cabbages.append((x,y))
        arr[x][y] = 1
    
    # print(cabbages)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    
    
    visited = [[False] * M for _ in range(N)]
    warm = 0
    # 
    for (x, y) in cabbages:
        if arr[x][y] == 1 and visited[x][y] == False:
            bfs(x,y)
            warm += 1

    print(warm)