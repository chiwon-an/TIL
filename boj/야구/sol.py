
'''
4번 타자는 고정!
다른 선수들의 타순을 정해서 가장 많은 득점을 하는 타순을 찾고, 그 때의 득점을 구해보자.
안타: 1 = 타자와 모든 주자가 한 루씩 진루한다.
2루타: 2 = 
3루타: 3
홈런: 4
아웃: 0

시간복잡도 계산은 못하니까 패스
득점 = 홈으로 들어오는 것을 의미

3아웃 제도

잔루를 제일 적게 해야함.
DFS문제인데, 결국 모든 경우의 수를 해주는 것이 좋을듯.

1. 종료 조건
    - 끝까지 정렬
    - 최댓값 갱신

2. out이 하나 있어서 3개가 되면 이닝 종료!
    루를 뜻하는 리스트를 하나 만들어주면 좋을듯.
    
    [0,0,0,0]

    저렇게 만들어주고, 

    두 번째 방법

    입력을 큐로 만들어 -> 들어간 것부터 하나씩 꺼내 -> 결과값에 하나씩 붙여주는데, 결과값에 붙이고 그 입력 값을 기존의 모든 결과값에 더해
    -> 결과 값에 4이상인 값들이 몇 개가 있는지를 새 -> 0을 3개 만나면 아웃.

    발견한 문제점 = 한 타순에 0이 3개보다 적은 것들이 있음.. -> 그럼 뺀 것들을 다시 큐의 맨 위에 붙이는 작업이 필요할 듯.

3. 정렬은 일단 기본적으로 0을 제일 뒤쪽으로 다 밀고 시작 -> sort?


1 - 입력 값들을 순열로 만들어.
    조건) 0은 맨 뒤로 놓는게 효과적 (선택)

2 - 조합으로 만들어진 리스트를 큐로 선언. -> 위와 같이 생각
'''
from itertools import permutations
from collections import deque
import sys

sys.stdin = open('input.txt','r')


def find_score(lineup, score, out, runner):

    lineup = deque(lineup, maxlen= 9)

    while out < 3:
        hit = lineup.popleft()

        # 아웃
        if hit == 0:
            out += 1
        
        # 안타
        elif hit == 1:
            if runner[2] == 1:
                score += 1
                runner[2] = 0
            
            if runner[1] == 1:
                runner[2] = 1
                runner[1] = 0
            
            if runner[0] == 1:
                runner[1] = 1
                runner[0] = 0
            
            runner[0] = 1
        
        # 2루타
        elif hit == 2:
            if runner[2] == 1:
                score += 1
                runner[2] = 0
            
            if runner[1] == 1:
                score += 1
                runner[1] = 0
            
            if runner[0] == 1:
                runner[2] = 1
                runner[0] = 0
            
            runner[1] = 1

        # 3루타
        elif hit == 3:
            if runner[2] == 1:
                score += 1
                runner[2] = 0
            
            if runner[1] == 1:
                score += 1
                runner[1] = 0
            
            if runner[0] == 1:
                score += 1
                runner[0] = 0
            
            runner[2] = 1

        elif hit == 4:
            score += sum(runner) + 1
        
        lineup.append(hit)
    
    return score


# 이닝 수 입력 받기
N = int(input())


# hitter = [list(map(int, input().split())) for _ in range(N)]
max_game_score = 0
for i in range(N):

    # 다 일단 입력 받아버리기.
    hitters = list(map(int, input().split()))
    best_player = hitters.pop(0)
    # hitter.sort(reverse=True)
    # hitter.insert(3,best_player)

    hitters = set(permutations(hitters,8))
    # print(hitters)

    max_score = -1

    for hitter in hitters:
        
        if hitter[0] == hitter[1] == hitter[2] == 0:
            continue
        
        lineup = list(hitter)
        lineup.insert(3,best_player)
        score = find_score(lineup, 0, 0, [0,0,0])
        # print(score)
        max_score = max(max_score, score)
        # game_score += max_score
        max_game_score = max(max_score, max_game_score)
        
print(max_game_score)