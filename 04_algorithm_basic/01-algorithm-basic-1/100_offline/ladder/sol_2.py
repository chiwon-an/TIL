import sys
sys.stdin = open('input (3).txt', 'r')

for test_case in range(1, 11):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
 
    for i in range(100):
        if data[99][i] == 2:
            row, col = 99, i
            break
 
    while row > 0:
        # 왼쪽으로 계속 이동
        if col > 0 and data[row][col - 1] == 1:
            while col > 0 and data[row][col - 1] == 1:
                col -= 1
        # 오른쪽으로 계속 이동
        elif col < 99 and data[row][col + 1] == 1:
            while col < 99 and data[row][col + 1] == 1:
                col += 1
        # 위로 한 칸
        row -= 1
 
    print(f'#{test_case} {col}')