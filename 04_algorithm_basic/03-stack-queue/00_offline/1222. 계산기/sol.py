import sys
sys.stdin = open('input.txt','r')
for tc in range(1,11):
    N = int(input())
    cal = list(map(str, input().strip()))
    # print(cal)

    sum_num = 0

    for k in range(0, N, 2):
        sum_num += int(cal[k])

    print(f'#{tc} {sum_num}')