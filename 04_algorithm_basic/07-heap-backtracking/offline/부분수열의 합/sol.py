import sys
sys.stdin = open('sample_input.txt', 'r')
'''
dfs
k가 되면 cnt에 1을 더해주고 return

그게 아니면 일단 현재까지 num_sum에 그걸 더해줘서 다음 재귀로 보내줘야지.

'''
def find_dfs(num_sum):

    global cnt

    # 가지치기
    if num_sum > K:
        return

    # 종료 조건
    if num_sum == K:
        cnt += 1
        return

    # 여기서 할 일
    for i in range(N):
        find_dfs(num_sum + idx_lst[i][1])


T = int(input())


for tc in range(1,T+1):
    
    N, K = map(int, input().split())

    lst = list(map(int, input().split()))
    # print(lst)
    idx_lst = []
    for i in range(N):
        idx_lst.append((i, lst[i]))
    cnt = 0
    # print(idx_lst)
    result = 0
    find_dfs(0)
    print(f'#{tc} {cnt//4}')