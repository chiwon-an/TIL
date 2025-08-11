'''
미로 문제임.
범위를 벗어나는 경우는 없을 것으로 생각됨.
0이면 길 / 1이면 벽 / 2이면 시작 / 3이면 도착

종료 조건
nx, ny가 3이면 종료 return 1

실행조건
1. visited행렬 생성(글로벌)
2. for문으로 상하좌우 조건 만들어준 뒤, nx, ny 생성
3. nx, ny의 visited가 false인지 판단
4. if false이면 visited = true 
5. nx, ny로 진출(회귀)
6. 갔다오고 난 뒤에는 visited에 다시 false해주기
7. 함수 맨 밑에 return 0

'''
import sys
sys.stdin = open('input (4).txt', 'r')


def find_goal(x,y):

  
    # 종료 조건
    if miro[x][y] == 3:
        return 1
    
    visited[x][y] = True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if visited[nx][ny] == False and miro[nx][ny] != 1:
            if find_goal(nx, ny) == 1:
                return 1
            # visited[nx][ny] = False

    return 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for tc in range(1,11):
    
    T = int(input())

    miro = [list(map(int, input())) for _ in range(16)]

    visited = [[False] * 16 for _ in range(16)]

    result = find_goal(1,1)

    print(f'#{tc} {result}')