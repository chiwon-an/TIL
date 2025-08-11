import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(start, s):
    global cnt
    if s == K:          # 합이 정확히 K면 1개 카운트
        cnt += 1
        return
    if s > K:           # 가지치기(모두 양수 가정)
        return
    for i in range(start, N):
        dfs(i + 1, s + lst[i])   # i를 선택하고, 다음엔 i+1부터

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)
    print(f'#{tc} {cnt}')