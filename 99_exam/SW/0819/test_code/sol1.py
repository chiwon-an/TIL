import sys
sys.stdin = open('sample_input (1).txt', 'r')

# def find_days():
    
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 나무 높이 받기
    trees = list(map(int, input().split()))
    # print(trees)
    
    # 제일 높은 값
    target = max(trees)

    # 차이를 구한다.
    diff = []
    for tree in trees:
        diff.append(target - tree)
    
    if sum(diff) == 0:
        print(f'#{tc} 0')
        continue
    
    # print(diff)

    holsu = []
    zacsu = []

    for dif in diff:
        if dif == 0:
            continue

        elif dif // 2 == 1:
            holsu.append(dif)

        elif dif // 2 == 0:
            zacsu.append(dif)
    
    # 최소 need_day일은 홀수 물주기 횟수를 만족해야 하므로
    need_day = holsu
    day = 0
    
    for dif in diff:

        if day % 2 == 1:

            if dif // 2 == 1:
                




            elif dif // 2 == 1:

