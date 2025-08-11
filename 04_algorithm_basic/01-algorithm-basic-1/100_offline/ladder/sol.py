# 밑에서부터 올라가기

'''
가장 기본적인 접근 방식은 밑에서부터 차근차근 올라가기

구현 알고리즘
1. 2를 찾기
2. 2를 찾았으면 거기서부터 1을 따라 올라가기
3. 올라가긴 가는데 갈 때 탐색을 왼쪽이나 오른쪽을 먼저하고, 왼쪽이나 오른쪽에 값이 있으면 그쪽으로 가기.
4. 그러면 결국 x 좌표값이 0이 될 때가 나올텐데, 거기서 y값을 찾기
DFS 사용 ! -> 이건 전체 다 보내는 건데, 좀 비효율적 아님?

'''

import sys
sys.stdin = open('input (3).txt', 'r')

# # 상 좌 우
# dx = [-1, 0, 0]
# dy = [0, -1, 1]


def find_start(nx, ny):

    # 종료 조건
    if nx == 0:
        return ny
    
    visited[nx][ny] = True

    # 현재 조건일 때 할 수 있는 모든 수

    # 좌
    if ny >= 1 and game[nx][ny-1] == 1 and visited[nx][ny-1] == False:
        nx = nx
        ny = ny - 1
    
    # 우
    elif ny <= 98 and game[nx][ny+1] == 1 and visited[nx][ny+1] == False:
        nx = nx
        ny = ny + 1
    
    # 상
    else: 
        nx = nx - 1
        ny = ny
    
    return find_start(nx, ny)


for _ in range(10):
    
    # tc 입력 받기
    tc = int(input())
    game = [list(map(int, input().split())) for _ in range(100)]

    # 목표지점 찾기
    goal = game[99].index(2)

    # 좌우 무한루프 돌 수도 있으니까, visited행렬 써주기
    visited = [[False] * 100 for _ in range(100)]


    print(f'#{tc} {find_start(99, goal)}')