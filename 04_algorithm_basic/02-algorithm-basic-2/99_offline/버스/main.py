# 전 좌표를 받아올 필요가 있음..
import sys
sys.stdin = open("sample_input.txt", 'r')

def find_next_step(start, K, station):

    if start >= len(station) - 1:
        return 0

    for step in range(K, 0, -1):
        next_step = start + step
        if next_step < len(station):
            if station[next_step] == 1:
                return 1 + find_next_step(next_step, K, station)

    return float('inf')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 버스정류장 리스트 생성
    station = [0] * (N+1)
    # print((station))

    # 충전기 위치 리스트로 받기
    charger = list(map(int, input().split()))
    # print(charger)

    # station에 충전소 표시하기
    for i in charger:
        station[i] = 1
    result = find_next_step(0, K, station)

    if result == float('inf'):
        print(f'#{tc} 0')

    else:print(f'#{tc} {result}')





# # print(station)
# count = 0
# next = 0
# for i in range(N):
#     for j in range(K, 0, -1):
#         if i + j > N:
#             continue
#         elif station[i+j] == 1:
#             next = i+j
#             count += 1
#             break
#
