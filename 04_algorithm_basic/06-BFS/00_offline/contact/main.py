import sys
sys.stdin = open('input (1).txt', 'r')

for tc in range(1,11):
    # N, start = map(int, input())
    #
    # numbers = map(int, input())
    # contact = {i:[] for i in range(1,101)}
    #
    # for i in range(0, N, 2):
    #     contact[numbers[i]].append(numbers[i+1])
    #
    # print(contact)
    # # for i in range(len(lst)):
    # #     if i % 2 == 0:
    # #         adj_list

    n, s = map(int, input().split())
    numbers = list(map(int, input().split()))

    contact = {i: [] for i in range(1, 101)}
    for i in range(0, n, 2):
        contact[numbers[i]].append(numbers[i + 1])




    # print(f'#{tc} {result})