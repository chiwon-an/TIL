import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

def qu():

    queue = deque(enter)
    line = deque([])
    result = 0
    parking = []

    while queue:
        cur = queue.popleft()

        # 주차장이 꽉차지 않았을 때
        if len(parking) < n or 0 in parking:

            # 지금꺼가 들어오는 거라면? -> 넣어주고 돈 받기
            if cur > 0:

                # 만약 낮은 자리가 없다면?
                if 0 not in parking:
                    parking.append(cur)
                    idx_cur = parking.index(cur)
                    result +=  weight[cur - 1] * cost[idx_cur]

                # 만약 0이 있다면?
                else:
                    idx_1 = parking.index(0)
                    parking[idx_1] = cur
                    result += weight[cur - 1] * cost[idx_1]


            # 나가는 거라면? 빼주기
            elif cur < 0:

                # idx를 받아와서 0으로 만들어주기
                idx = parking.index(-cur)
                parking[idx] = 0

                # 만약 대기 줄이 있었다면 대기줄을 최상단으로 넣어주기
                if len(line) != 0:
                    a = line.popleft()
                    queue.appendleft(a)

        # 주차장이 꽉 찼을 때
        elif len(parking) == n and 0 not in parking:

            # 나가는 거면 나가시오.
            if cur < 0:
                idx = parking.index(-cur)
                parking[idx] = 0

                # 만약 대기 줄이 있었다면 대기줄을 최상단으로 넣어주기
                if len(line) != 0:
                    a = line.popleft()
                    queue.appendleft(a)

            # 들어오는 거라면 기다리는 거에 추가
            elif cur > 0:
                line.append(cur)

    return result


T = int(input())

for tc in range(1, T+1):

    n, m = map(int, input().split())

    # 단위 요금 당 요금
    cost = [int(input()) for _ in range(n)]

    # 각 자동차별 무게
    weight = [int(input()) for _ in range(m)]

    # 출입 로그
    enter = [int(input()) for _ in range(2*m)]
    
    b = qu()
    print(f'#{tc} {b}')