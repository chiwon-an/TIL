'''
한 번이라도 공격받은 외양간은 방어에 취약해져, 수리하기 전까지 매일 밤 일정 수의 소를 잃게 됩니다.
김씨는 하루에 한 명의 기술자만 부를 수 있어, 여러 외양간의 수리를 동시에 시작할 수 없습니다.
한 외양간의 수리를 시작하면, 정해진 수리 기간이 끝날 때까지 다른 외양간의 수리를 시작할 수 없습니다.

총 M일간 늑대의 습격이 예정되어 있을 때, 김씨는 어떤 순서로 외양간을 고쳐야 소의 총 피해를 최소화할 수 있을까?

N개의 외양간
    - 일일 손실량 ("Li"): 한 번 공격받은 후, 수리가 완료되기 전까지 매일 밤 잃게 되는 소의 마릿수입니다.
    - 수리 기간 ("Di"): 해당 외양간을 수리하는 데 걸리는 기간(일)입니다.

총 M일 동안 매일 밤, 늑대는 정해진 순서에 따라 단 하나의 외양간을 공격
    - '취약 상태가 아닌' 외양간만 공격 대상
    - "d"번째 날 밤에 "Ad"번 외양간이 공격당하면, 해당 외양간은 그날 밤부터 '취약 상태'

농부는 다음 날 아침부터 수리를 시작할 수 있습니다.
    - 농부는 아침에 '취약 상태'인 외양간 중 하나를 골라 수리를 시작할 수 있습니다.
    - 만약 다른 외양간을 수리하는 중이라면, 새로운 수리를 시작할 수 없습니다.
    - "i"번 외양간의 수리를 시작하면 "Di"일 동안 수리가 진행되며, "Di"일이 지난 다음 날 아침부터 다른 외양간 수리를 시작할 수 있습니다.

N, M = 외양간 갯수, 전체 일 수

N줄
    Li, Di = 일일 손실량, 수리 기간

M줄
    d번째 날 밤에 공격 받는 외양간의 번호


소의 손실을 최소화하는 값을 출력하시오.

<알고리즘>

매일 밤마다 내가 어떤 선택을 하는게 좋을지 선택 -> 그리디

매 아침마다 어떤 선택을 하는게 최선일까? -> 

or DFS로 완전 탐색시켜서, 공격을 당하면 고치지 않는 경우와 고치는 경우, 이 두 갈래로 나뉘어서 완전 탐색시키기 -> 최적의 값에 도달했다 ? -> 그럼 BFS로 

BFS
    1. 종료 조건 = 
    2. visited 구현하기
    3. 


ATTACK
    1. 하루에 한 번은 공격을 받음
    2. attacks에서 day인덱스로 값을 빼와서
    3. 그 값을 homes의 인덱스로 접근
    4. 그 home의 arr의 일일 손실량만큼 손실량에 더해주기 

REPAIR
    1. 공격을 받았다면, 그걸 고칠지 말지를 판단
    2. 여기서 bfs로 접근
    3. 고칠 경우와 안 고칠 경우로 두 갈래길로 재귀
    4. 고칠 경우? -> 지금 수리 중인 외양간이 없는 조건 하에 고칠 수 있음.
    5. 수리 중인 경우를 판단하기 위해 배열을 하나 만들어서 그 값의 길이가 1이라면 고칠 수 없는 거고, 0이라면 고칠 수 있는 거임. 근데 고칠 수 있어도 안 고치는 경우가 있어야 됨.
    6. 나머지는 그냥 고치지 않기로 판단한 것.
    7. 고칠 경우
        - damaged 배열도 넣어주기
        - 그 수리 중이라는 배열에서 그 값이 필요한 arr[번호][1]이 지나면, 배열에서 pop해주기.

    8. 안 고칠 경우
        - damaged 배열 넣어주기
    
    9. day가 지날 때마다 damaged배열에 모든 값을 더해서 sum(damaged)해서 누적 값에 넣어주기

    * 참고 = damaged배열은 초기 값을 0으로 설정해주고, 날마다 추가되면 일일 손실량을 넣어주기

<자료구조>

day = 0
arr[][] = 2차원 리스트로 만들어서, 한 행의 [0]은 일일 손실량, [1]은 수리 기간
attacks[day-1] = 1차원 리스트, 순서대로 공격 받는 외양간 번호임.
homes = list(range(N+1))
repairing = []
damaged = []

애초에 받을 때 N-1로 해주는게 덜 헷갈릴 것 같은데,, 


'''

import sys
sys.stdin = open('sample_input.txt', 'r')

def bfs(day, damaged, repairing, cnt):

    global result

    if day == M:
        result.append(cnt)
        return

    # 순서대로 공격!
    cur_attack = attacks.pop()
    damaged_home.append(cur_attack)
    # damaged 리스트에 일일 손실량 넣어주기
    damaged[cur_attack] = arr[cur_attack][0]
    cnt += sum(damaged)

    # 다 고쳤으면 빼주기.
    if repairing == 0 and len(repairing_home) != 0:
        temp = repairing_home.pop()
        damaged[temp] = 0

    # 못 고칠 경우
    if len(repairing_home) != 0:
        bfs(day+1, damaged, repairing -1, cnt)
        

    # 고칠 경우
    elif repairing == 0 and len(repairing_home) == 0:

        # 고쳐야 하는게 쌓여 있을 수 있잖아. 그걸 하나씩 다 해줘야함.
        for item in damaged_home:
            repairing = arr[item][1]
            repairing_home.append(item)
            bfs(day + 1, damaged, repairing, cnt)


T = int(input())

for tc in range(1,T+1):

    # N, M = 외양간 갯수, 전체 일 수
    N, M = map(int, input().split())

    # arr[][] = 각 외양간 번호가 행의 번호 / 한 행의 [0]은 일일 손실량, [1]은 수리 기간
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # pop 하기 편하게 뒤로 순서를 바꿔줬음.
    # 값들도 0부터 시작하기 위해서 1씩 빼줬음.
    # 1번집 -> 0번집
    attacks = [int(input()) -1 for _ in range(M)]
    attacks.reverse()
    # print(attacks)

    # 계속 올라갈 day선언
    day = 0
    homes = list(range(N+1))
    repairing = 0
    repairing_home = []
    damaged = [0] * N
    result = []
    cnt = 0
    damaged_home = []

    bfs(day, damaged, repairing, cnt)
    print(result)