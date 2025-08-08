'''
문제
4×4 크기의 격자판 / 0부터 9 사이의 숫자

격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.

이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 됨.

단, 격자판을 벗어나는 이동 X

격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.
---------------------------------------------------

이건 무조건 dfs 문제일 수밖에 없음.
왜냐 ? -> 모든 경우의 수를 탐색하는 문제이기 떄문에.

DFS를 어떻게 쓸 건지를 판단.
1. 임의의 위치에서 시작해서 전체를 다 한 번씩 갈 수 있는 로직.
    1-1. 범위 조건은 격자판 내에 있어야 함.

2. 임의의 위치에 도착했을 떄 상, 하, 좌, 우의 숫자를 가져와서 아마 작게는 2개에서 4개까지의 숫자들로 본인을 포함한 7자리 숫자의 조합의 갯수를 구하기 (순열)

3.

'''
import sys
from itertools import product
sys.stdin = open('sample_input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_find_index(arr, x, y):

    global result
    global cnt
    # 종료 조건
    if True not in visited:
        return cnt

    # 현재 조건에서 할 일
    visited[x][y] = True

    # 주변에 있는 값을 가져오기.
    for k in range(4):
        nx = x +dx[k]
        ny = y + dy[k]

        # 주변 값이 arr 내에 있는 값이면 result에 값을 집어 넣어라.
        if  0 <= nx < 4 and 0 <= ny < 4:
            result.append(arr[nx][ny])

        # 주변 값이 arr 밖에 있는 거면 이번건 패스.
        else: continue

    # result에 담긴 주변 값들에서 본인을 포함한 7자리 숫자의 조합의 갯수를 구하기.
    # 본인까지 넣어주기.
    result.append(arr[x][y])

    # cnt에 7자리 수 넣어놓기.
    cnt.append(list(product(result, repeat= 7)))

    # 다음 거 찾으러 가기
    for k in range(4):
        nx = x +dx[k]
        ny = y + dy[k]

        if  0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny] == False:
            dfs_find_index(arr, nx, ny)

        else: return


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    visited =[[False] * 4 for _ in range(4)]
    result = []
    cnt = []
    dfs_find_index(arr, 0, 0)
    print(cnt)