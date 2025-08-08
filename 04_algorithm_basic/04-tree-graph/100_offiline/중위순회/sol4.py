import sys
sys.stdin = open('input.txt', 'r')


def inorder(tree,idx):

    if idx > n or idx < 1 :
        return
    inorder(tree, 2*idx)
    print(tree[idx][1], end='')
    inorder(tree,2*idx + 1)

for tc in range(1,11):

    n = int(input())

    tree = [0] + [list(map(str, input().split())) for _ in range(n)]


    print(f'#{tc}', end =' ')
    inorder(tree, 1)
    print( )