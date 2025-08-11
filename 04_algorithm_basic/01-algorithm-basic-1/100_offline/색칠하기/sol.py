'''
영역을 맞추는 문제임
해당 좌표 값이 들어온다면, 사각형의 크기를 구할 수 있겠지?
그 사각형만큼 + 1을 해주자.
그렇게 N번 하면, 겹쳐진 부분은 N값이 될 거잖아?
그러면 N값의 갯수를 구해주면 될듯?
일단 ㄱㄱ
'''

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    
    # 색칠 갯수    
    N = int(input())

    # 인풋을 담아놓을 리스트
    # input_list = []

    # 결과를 담아줄 리스트
    result = [[0] * 11 for _ in range(11)]

    for _ in range(N):
        temp = list(map(int, input().split()))


        width = temp[2] - temp[0] + 1 
        height = temp[3] - temp[1] + 1

        for i in range(width):
            for j in range(height):
                
                result[temp[0] + i][temp[1]+j] += temp[4]

    cnt = 0
    for row in result:
        for i in row:
            if i >= 3:
                cnt += 1


    print(f'#{tc} {cnt}')
