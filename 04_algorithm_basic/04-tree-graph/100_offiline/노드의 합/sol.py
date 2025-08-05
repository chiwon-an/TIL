import sys
sys.stdin = open('input.txt','r')

# 주어진 값을 찾고자 하는 함수
def postorder_traversal(idx):
    
    # N보다 크면 없는 것.
    if idx > N:
        return 0

    # 만약 N이 None이 아니면 return으로 그 값을 반환
    if tree[idx] != 0:
        return tree[idx]

    # 둘 다 아니면, 자식 노드들을 left, right에 할당해줌.
    # 자식 노드들도 없을 수 있잖아. 따라서 여기서 재귀함수를 할당.
    left = postorder_traversal(idx * 2)
    right = postorder_traversal(idx * 2 + 1)

    # 위에 재귀함수로 left, right를 가져왔으면,
    tree[idx] = left + right
    return tree[idx]

T = int(input())

for tc in range(1,T+1):
    
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)

    #트리 구조로 리스트 생성
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    # 어떻게 해야할까 -> 밑에서부터 재귀적으로 점점 더해서 올라와야 할 것 같아. if 그 값이 없다면 sum에 더해라. 이런 식으로
    
    result = postorder_traversal(L)
    print(f'{tc} {result}')
    
    