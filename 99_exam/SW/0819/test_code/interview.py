'''
N개의 문제가 순차적으로 주어지는 면접에서 문제들 중 정확히 M개를 맞추었다.
어떤 문제들을 맞추었는지는 기억이 안 나지만 정확히 M개를 맞추었다는 것은 사실이다.
이 면접에서는 연속으로 문제를 맞추는 경우 점수를 더 많이 준다.

1. 카운터의 값은 처음에 0이다.
2. 문제를 틀리는 경우, 카운터는 항상 0으로 리셋되고 해당 문제에 대해서는 0점이 부여된다.
3. 문제를 맞추는 경우, 카운터는 1 증가되고 해당 문제에 대해서는 1점이 더해진다.
4. 카운터가 주어진 K가 된 경우, 해당 문제에 대해 1점이 더해지고, 카운터는 0으로 리셋되면서 동시에 전체 점수가 2배가 된다.

철수가 M개의 문제를 맞추는 모든 가능한 경우들 중 받은 총점이 최소인 경우를 찾아 그 점수를 제시하라.

[제약사항]
1.	N은 3 이상 500 이하이다. (3 ≤ N ≤ 500)
2.	M과 K는 2 이상 N 이하의 값이다.
3.	풀이가 불가능한 경우는 주어지지 않는다.
4.	답은 32비트 int의 범위를 넘지 않음이 보장된다.

<아이디어>
완전 탐색으로 해야될 것 같음.
맞는 것 = 1 / 틀린 거 = 0
순열을 돌려야 할 것 같다.
set으로 중복을 제거시키기.
그럼 맞고 틀리는 모든 경우의 수를 찾을 수 있음.
그러면 여기서 카운터를 적용시켜서 가장 작은 값만 갱신 시키기.
'''

from itertools import permutations
import sys
sys.stdin = open('Sample_input.txt', 'r')

def permutation():



def counter(item):
    global K
    score = 0
    count = 0
    for i in range(N):
        # K
        if count != K and item[i] == 1:
            score += 1
            count += 1

        if count != K and item[i] == 0:
            count = 0

        if count == K and item[i] == 1:
            # print(score)
            # score += 1
            score *= 2
            count = 0

        if count == K and item[i] == 0:
            count = 0

    return score


# 테스크 케이스 입력 받기
T = int(input())

# 테스트 케이스만큼 반복
for tc in range(1, T+1):

    N, M, K = map(int, input().split())
    min_score = float('inf')
    # print(N, M, K)

    # 맞춘 갯수만큼 1 넣기, 틀린 갯수만큼 0 넣기
    solve = [1]*M + [0]*(N-M)

    # 중복을 제거해서 solve 넣기 완료
    solve = set(permutations(solve, N))
    # solve = list(solve)
    for item in solve:
        # counter(item)
        min_score = min(min_score, counter(item))

    print(f'#{tc} {min_score}')