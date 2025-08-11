'''
주어진 일이 모두 성공할 확률의 최댓값

퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력

이런 dfs로 완전 탐색 해야할듯.

1번이 뭘 선택했을 때 다른 사람들이 선택했을 모든 경우의 수에 따라서 최대값 출력
  0   1    2   3
[[71, 51, 30, 1],  0번째 사람이 성공할 확률
[29, 63, 32, 93],  1번째 사람이 성공할 확률
[84, 94, 33, 21],  2번째 사람이 성공할 확률
[56, 40, 80, 31]]  3번째 사람이 성공할 확률
'''
import sys
sys.stdin = open('input.txt','r')


def find_percent(x):

    global max_percent
    global result

    # 가지치기
    if result <= max_percent:
        return

    # 탈출 조건
    if x == N:
        if result > max_percent:
            max_percent = result     
        return    
        # max_percent = max(result, max_percent)
        # return

    # 현재 값에서 할 동작들
    # 1행에서 선택한 열을 다른 행들은 선택할 수 없다는 것이 포인트인듯.
    
    for j in range(N):

        if visited[j] == False:
            visited[j] = True
            # result도 초기화 해줘야 함.
            prev = result
            result *= percent[x][j]      
            find_percent(x+1)
            result = prev
            visited[j] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    percent = [list(map(lambda v: int(v) / 100.0, input().split())) for _ in range(N)]
    print(percent)
    result = 1.0
    visited = [False] * (N)


    max_percent = 0.0
    find_percent(0)
    print(f'#{tc} {max_percent * 100:.6f}')