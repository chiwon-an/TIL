import sys
sys.stdin = open('input.txt', 'r')

def find_complict(x_idx, y_idx):

    # 충돌 갯수 세기
    global cnt

    while x_idx <= 99:

        # 2를 만나면 하나 추가! AND 끝 !
        if arr[x_idx][y_idx] == 2:
            cnt += 1
            return cnt

        # 2를 만나지 못하고 1을 만났으면 이건 그냥 pass
        if arr[x_idx][y_idx] == 1:
            return

        # 0이면 그냥 pass 사실 없어도 되는 조건
        if arr[x_idx][y_idx] == 0:
            pass

        x_idx += 1

for tc in range(1, 11):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    idx_red = []
    cnt = 0

    # 빨강색 다 찾기 완료 리스트 내 튜플 형태로 담아놓음
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                find_complict(i+1,j)

    print(f'#{tc} {cnt}')


