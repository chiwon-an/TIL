import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

# code암호화 해결 딕셔너리
code = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(str, input())) for _ in range(N)]

    # 오른쪽 코드가 다 1로 끝나니까 오른쪽부터 탐색실시

    for i in range(N):
        result = []
        # 리스트에 1이 있는 행 하나만 반환
        if '1' in lst[i]:
            result = lst[i]
            break

    # print(result)

    # M부터 1씩 감소하면서 최초로 1이 나오는 인덱스를 반환
    for i in range(M-1,-1,-1):
        if result[i] == 1:
            idx = i
            break

    # 암호를 해독한 결과를 넣어줄 리스트
    result_1 = []
    for i in range(idx, idx-56, -7):
        pattern = ''.join(result[i:i + 7])
        result_1.append(code[pattern])

        # # 7자리 수가 있으니까 그걸 하나로 합쳐.
        # for j in range(7):
        #     number += result[k-j]
        #
        #