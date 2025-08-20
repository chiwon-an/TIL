'''
나무의 키
N  = 나무의 갯수

하루에 한 나무에 물을 줄 수 있다.

홀수 번째 날은 키가 1 자라고 짝수 번째 날은 키가 2 자란다.

모든 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 할 수 있는 최소 날짜 수를 계산

어떤 날에는 물을 주는 것을 하지 않을 수도 있다.

첫째 날에 물을 주게 되면, 나무의 높이를 모두 4로 만들기 위해서는 3일째까지 물을 주어야 한다.
둘째 날은 아무 일도 안 하게 된다. 하지만, 첫째 날을 쉬고 둘째 날에 물을 주면 2일 만에 나무의 높이가 모두 4가 된다.

<제약조건>
1. 나무의 개수 N은 2 이상 100 이하이다. (2 ≤ N ≤ 100)
2. 주어지는 나무의 초기 높이는 1 이상 120 이하이다.

<아이디어>

BFS가 맞는 것 같음.

1. 일단 입력을 받고 거기서 제일 큰 나무를 저장을 해둬야 함.
2. 홀수 번째 날이라면, 0 OR 1을 선택할 수 있고,
3. 짝수번째 날이라면, 0 OR 2을 선택할 수 있음.

BFS -> 매개변수 day로 처음엔 1
    -> day가 짝수라면 0 or 2 두가지 선택지
    -> day가 홀수라면 0 or 1 두가지 선택지
    -> 선택지마다 하나씩 다 돌면서 더하기 하는 그 걸 구현하기
    -> 종료조건 = 모든 tree가 목표와 같아질 때까지
    ->

'''

import sys
sys.stdin = open('sample_input (1).txt', 'r')

def dfs(target, day, trees, i):

    global visited

    # 모든 트리가 목표 값이 되었으면
    if set(trees) == target:
        return day

    if trees[i] == target:
        visited[i] = True
        return

    if day % 2 == 0 and visited[i] == False:
        trees[i] += 2
        dfs(target, day+1, trees, i)
        trees[i] -= 2

        dfs(target, day+1, trees, i)

    elif day % 2 == 1 and visited[i] == False:
        trees[i] += 1
        dfs(target, day + 1, trees, i)
        trees[i] -= 1

        dfs(target, day + 1, trees, i)

# 테스크 케이스 입력 받기
T = int(input())

# 테스트 케이스만큼 반복
for tc in range(1, T+1):

    N = int(input())
    visited = [False] * N
    trees = list(map(int, input().split()))
    target = max(trees)

    print(dfs(target, 0, trees, 0))

    # for i in range(N-1):
    #     if trees[i] == target:
    #         trees.pop(i)

    # print(trees)