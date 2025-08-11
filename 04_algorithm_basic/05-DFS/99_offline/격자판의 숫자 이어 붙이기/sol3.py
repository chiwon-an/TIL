import sys
sys.stdin = open('sample_input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_number(x, y, number):

    global result

    # 종료 조건
    if len(number) == 7:
        result.add(number)
        return

    # 할 일
    for k in range(4):

        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 4 and 0 <= ny < 4:
            find_number(nx, ny, number + arr[nx][ny])
            


T = int(input())

for tc in range(1, T+1):
    
    arr = [list(map(str, input().split())) for _ in range(4)]

    result = set()

    for x in range(4):
        for y in range(4):
            find_number(x, y, '')
    
    print(f'#{tc} {len(result)}')