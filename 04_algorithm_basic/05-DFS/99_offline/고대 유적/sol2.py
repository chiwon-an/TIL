import sys
sys.stdin = open('input1.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]


    # for row in arr:
    #     for i in range(M-1):
    #         if row[i] == 1 and row[i+1] == 1:
    #             cnt += 1
    #         else:

    idx = []

    for x, row in enumerate(arr):
        for y, val in enumerate(row):
            if arr[x][y] == 1:
                idx.append((x,y))

    # print(idx)

    length = 0

    # for i in range(N):
    #     for j in range(M):
            
    print(idx[0][0])
