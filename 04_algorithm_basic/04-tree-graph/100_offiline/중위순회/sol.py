import sys
sys.stdin = open('input.txt','r')

def inorder_traversal(idx):
    '''
        중위 순회란, 부모 노드 차례가 중간인 순회 방식
        즉, 왼쪽 서브 트리에 대한 처리가 우선 되어야 한다.
    '''
    # 어디까지 순회해야 하나?
    # 순회 대상의 범위를 벗아나지 않았다면!
    if idx <= N:
        # 왼쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2)
        # 중위 순회는 왼쪽 서브트리 순회 후에 조사한다.
        print(tree[idx], end='')
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2 + 1)


for tc in range(1, 11):

    N = int(input())

    tree = [None] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        user_input = list(map(str, input().split()))

        # 4개 입력인 경우
        if len(user_input) == 4:
            idx = int(user_input[0])
            val = user_input[1]
            left = int(user_input[2])
            right = int(user_input[3])
            tree[idx] = val

        # 3개 입력인 경우
        elif len(user_input) == 3:
            idx = int(user_input[0])
            val = user_input[1]
            left = int(user_input[2])
            tree[idx] = val

        # 2개 입력인 경우
        if len(user_input) == 2:
            idx = int(user_input[0])
            val = user_input[1]
            tree[idx] = val

    result = inorder_traversal(1)
    print(f'#{tc} {result}')