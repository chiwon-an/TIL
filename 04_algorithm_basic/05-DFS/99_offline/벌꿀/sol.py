import sys
sys.stdin = open('sample_input (3).txt','r')

def find_max_honey(x, y, idx, result):
    temp = []
    for i in range(M):
        # C보다 큰 것들은 완전 제거
        if honeys[x][y+i] > C:
            continue
        # C보다 작은 값들만 temp에 넣기
        else:
            temp.append(honeys[x][y+i])

    # 만약 다 더한 것들이 C보다 작다면
    if sum(temp) <= C:
        for item in temp:
            sum_honey += item**2
        result.append(sum_honey)
        return

    # 근데 이게 C보다 크다면?
    # 여기가 조합을 구할 타이밍인듯..
    # temp 리스트에 있는 것들 중에 더한 값이 C를 넘지 않는 조합들 중에서
    # 각자의 제곱의 합이 최대가 되는 것들을 뽑아주기 마지막 결과를 result로 반환
    find_combination()

def find_combination(temp):
    pass

# def find_optical_result():
#     pass

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]
    result = []
    idx = []
    for x in range(N):
        for y in range(N-M+1):
            find_max_honey(0, y, M, idx, result)

    print(f'#{tc} {result}')