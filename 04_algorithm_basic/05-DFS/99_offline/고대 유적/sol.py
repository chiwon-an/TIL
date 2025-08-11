'''
사진의 해상도는 NxM                                                                               -> N,M으로 입력 받으면 될듯
구조물이 있는 곳은 1, 빈 땅은 0으로 표시                                                            -> 
교차하거나 만나는 것처럼 보이는 구조물은 서로 다른 깊이에 묻힌 것이므로 직선인 구조물만 고려                -> 직선만 생각하기.
평행한 모든 구조물은 서로 1m이상 떨어져 있고, 구조물의 최소 크기는 1x2m                                 -> 최소 1을 찾으면 숫자로 입력 받아서 다 더해줘도 될 것 같음 OR 문자열로 입력 받아서 len함수
여러 구역의 사진 데이터가 주어질 때, 각 구역 별로 가장 긴 구조물의 길이를 찾는 프로그램                    -> 중간에 겹치는 부분도 있으니까, visited행렬은 쓰면 안됨.

DFS
1. 격자 내 아무 곳이나 찾아. -> 시작 좌표 = 0,0 OR 글로벌에서 1이 나오는 위치들만 넣어주기
2. 상하 / 좌우 나눠서 조사를 해야될 것 같음. 이 반복 내에서는 VISITED행렬이 필요할 것 같은데, 전체적으로는 없어야 할 것 같음...... 가운데 있는 1에 탐색했다가, 위로 갔다가 아래로 갔다가 반복될 수 있는 거 아님?
3. 그럼 그냥 하 / 우 이렇게만 조사하면 나올 것 같지 않음??
4. 탈출 조건은 depth가 조사 위치가 N,M이 될 때...? arr[nx][ny] 가 범위를 벗어나거나, 0이 될 때까지
'''

import sys
sys.stdin = open('input1.txt', 'r')

def dfs_x(x, y):
    # 전역: arr, N, M, cnt, result
    global cnt, result

    # 모든 열을 처리했으면 종료
    if y >= M:
        return

    # 한 열을 다 내려왔으면(= x가 경계 밖),
    # 지금까지의 run을 반영하고 다음 열로 넘어감
    if x >= N:
        if cnt > 0:
            result = max(result, cnt)
            cnt = 0
        dfs_x(0, y + 1)
        return

    # 현재 칸 처리
    if arr[x][y] == 1:
        # 1이면 run 연장
        cnt += 1
    else:
        # 0이면 현재 run 종료 → 반영하고 리셋
        if cnt > 0:
            result = max(result, cnt)
            cnt = 0

    # 같은 열에서 아래로 계속 진행
    dfs_x(x + 1, y)



def dfs_y(x, y):
    
    global result, cnt

    # 탈출조건

    if x >= N:
        return
    
    if y >= M:
        if cnt > 0:
            result = max(result, cnt)
            cnt = 0
    
        dfs_y(x+1, 0)
        return
    
    if arr[x][y] == 1:
        cnt += 1
    
    else:
        if cnt > 0:
            result = max(cnt, result)
            cnt = 0

    dfs_y(x, y+1)



T = int(input())

for tc in range(1, T+1):
    
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    result = 0

    dfs_x(0,0)
    dfs_y(0,0)

    print(f'#{tc} {result}')