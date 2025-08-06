import sys
sys.stdin = open('input (1).txt','r')

from collections import deque

#    상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_minimum_time(N):

    queue = deque()
    # x,y,time
    queue.append((0, 0, 0))

    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1

    while queue:
        row, col, time = queue.popleft()

        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            if nx == N-1 and ny == N-1:
                result.append(time)

            visited[nx][ny] = 1
            queue.append((nx, ny, time + arr[nx][ny]))

# 문제점 1 : visited가 함수 내 전역변수로 선언되어 있으므로, 다른 길로 갔음에도 visited에 있기 때문에 방문을 하지 못한다.
# 문제점 2 : 그렇다고 visited를 없애고, 전에 방문했던 곳을 방문하지 않는 걸로만 하면 시간 복잡도가 지수적으로 늘어난다.

# 해결 : time_map을 만들어줘서, 그 자리에 누군가가 왔을 때 그 전의 경로에 이것보다 작은 time으로 방문한 적이 있다면 이건 continue


T = int(input())

result = []

for tc in range(1, T+1):

    # 입력을 내가 원하는 데이터 타입으로 받기 완료
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # N에 대한 그걸 줘.
    find_minimum_time(N)

    # 최솟값 구하기.
    min_num = float('inf')

    for item in result:
        min_result = min(min_num, item)

    print(f'#{tc} {min_result}')