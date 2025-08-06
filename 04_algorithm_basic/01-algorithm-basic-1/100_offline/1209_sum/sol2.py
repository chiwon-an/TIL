import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


for tc in range(1,  T+1):
    
    # 2차원 배열 생성
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 가로 / 세로 / 대각선 중 최댓값 구하기


def row_sum(idx):
    if idx == len(arr):
        return max_row_sum
    
    else:
        arr[idx]
