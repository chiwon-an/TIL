# 완전 이진 트리 기준 순회

# 전위 순회
def preorder_traversal(idx):
    # 어디까지 순회해야 하나?
    # 순회 대사잉 범위를 벗아나지 않았다면!
    if idx <= N:
        # 전위 순회는 부모 노드를 먼저 조사한다.
        print(tree[idx], end=' ')
        # 이제 왼쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx * 2)
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx * 2 + 1)

# 중위 순회
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
        print(tree[idx], end=' ')
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2 + 1)

# 후위 순회
def postorder_traversal(idx):
    # 어디까지 순회해야 하나?
    # 순회 대상의 범위를 벗아나지 않았다면!
    if idx <= N:
        # 왼쪽 서브 트리에 대해서도 동일한 조건
        postorder_traversal(idx * 2)
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        postorder_traversal(idx * 2 + 1)
        # 후위 순회는 모든 서브트리 순회 후에 조사한다.
        print(tree[idx], end=' ')

N = 5
tree = [0, 'A', 'B', 'C', 'D', 'E']


'''
    트리 구조
        'A'
      /   \
   'B'    'C'
  /   \
'D'    'E'
'''

print('전위 순회')
# 트리를 결국 배열 형태로 만들것이고,
# 그 인덱스를 각 노드의 값이 삽입된 위치로 볼 것이기 떄문에,
# 루트노드에 해당하는 1번 인덱스부터 조회를 시작할 것이다.
preorder_traversal(1)  # 'A' 'B' 'D' 'E' 'C'
print()
print('중위 순회')
inorder_traversal(1)  # 'D' 'B' 'E' 'A' 'C'
print()
print('후위 순회')
postorder_traversal(1)  # 'D' 'E' 'B' 'C''A'