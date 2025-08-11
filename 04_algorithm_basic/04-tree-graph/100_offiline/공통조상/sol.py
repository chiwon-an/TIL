import sys
sys.stdin = open('input (5).txt', 'r')

'''
각 케이스의 첫 번째 줄에는 정점의 개수 V(10 ≤ V ≤ 10000)와 간선의 개수 E, 공통 조상을 찾는 두 개의 정점 번호가 주어진다.

각 케이스의 두 번째 줄에는 E개 간선이 나열된다. 간선은 항상 “부모 자식” 순서로 표기된다.

위에서 예로 든 트리에서 정점 5와 8을 잇는 간선은 “5 8”로 표기된다.

정점의 번호는 1부터 V까지의 정수이며, 루트 정점은 항상 1번이다.
'''

T = int(input())

for tc in range(1, T+1):
    V, E, number1, number2 = map(int, input().split())

    lst = list(map(int, input().split()))

    parent = []
    child = []
    node = dict()
    for i in range(0, len(lst), 2):

        if node.get(lst[i]):
            node[lst[i]] = node[lst[i]] + lst[i+1]
            

        else:
            node[lst[i]] = lst[i+1]

    print(node)

