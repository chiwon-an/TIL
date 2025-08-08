import sys
sys.stdin = open('input (1).txt','r')

def baby_gin(cnt_lst):
    if sum(cnt_lst) == 0:
        return 'true'

    for i in range(10):
        if cnt_lst[i] == 6:
            return 'true'

        if cnt_lst[i] >= 3:
            cnt_lst[i] -= 3
            return baby_gin(cnt_lst)
            cnt_lst[i] += 3

    for i in range(8):
        if cnt_lst[i] >= 1 and cnt_lst[i + 1] >= 1 and cnt_lst[i + 2] >= 1:
            cnt_lst[i] -= 1
            cnt_lst[i + 1] -= 1
            cnt_lst[i + 2] -= 1
            return baby_gin(cnt_lst)
            cnt_lst[i] += 1
            cnt_lst[i + 1] += 1
            cnt_lst[i + 2] += 1

    return 'false'

T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().strip()))
    cnt_lst = [0] * 10

    # print(cards)
    for card in cards:
        cnt_lst[card] += 1

    # print(cnt_lst)

    print(f'#{tc} {baby_gin(cnt_lst)}')