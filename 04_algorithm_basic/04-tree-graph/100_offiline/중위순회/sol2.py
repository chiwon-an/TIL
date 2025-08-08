import sys
sys.stdin = open('input.txt', 'r')

'''
문제를 딱 보면 중위순회를 해야하는 것을 알 수 있음.

중위 순회 뼈대 코드

중위 순회를 하는 처음 루트 노드를 지정해주면, 중위 순회해서 알아서 출력해라.
'''

def find_string(idx):
    if idx > N or tree[idx] == 0:
        return

    find_string(2*idx)
    print(tree[idx], end='')
    find_string(2*idx + 1)


for tc in range(1, 11):

    N = int(input())

    # 어쩔 수 없이 문자열로 받아버림
    user_input = [list(map(str, input().split())) for _ in range(N)]

    # print(user_input)
    tree = [0] * (N + 1)

    for i in range(N):
        tree[int(user_input[i][0])] = user_input[i][1]


    print(f'#{tc} ', end='')
    find_string(1)
    print()
