'''
색종이의 크기는 1x1, 2x2, 3x3, 4x4, 5x5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.
색종이를 크기가 10x10인 종이 위에 붙이려고 한다.
종이는 1x1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다.
1이 적힌 칸은 모두 색종이로 덮여져야 한다. 
색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다.
또, 칸의 경계와 일치하게 붙여야 한다.
0이 적힌 칸에는 색종이가 있으면 안 된다.
모든 1을 덮는데 필요한 색종이의 최소 개수를 출력한다. 1을 모두 덮는 것이 불가능한 경우에는 -1을 출력한다.
종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자.

<생각>
0위에 색종이를 덮을 수 없음 -> 사각형이 아니면 덮을 수가 없음.
1. 사각형인지 아닌지 판단.
    how?
    - dfs로 일단 하나씩 가. -> 오른쪽 아래 왼쪽 위 -> 1이 있을 만큼. 가로로 5개 갔는데, 아래로 3개 밖에 없어 -> 가로도 3개짜리로 
    - 
2. 사각형일시 ? -> 사각형 크기만큼의 1을 0으로 바꿔주기.
3. 사각형이 아닐시? -> 1짜리 소모.
4. 다 했는데도 안되면 없애기
'''
# 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_cnt(x,y,turned, direction):

    global rectangle
    
    # 탈출 조건
    # 3번 돌고 자기 자리에 왔으면 ? 사각형 완성
    if turned == 3 and x == sx and y ==sy:
        length = max(result_x) - min(result_x)
        
        while length ==0:
            

    # 색종이의 갯수가 -1이 됐으면 만들어질 수 없던 거임.
    if -1 in rectangle:
        return -1
    
    # 범위 밖이면 나가리
    if 0 > x or x >= N or 0 > y or y >= N:
        return

    # 0을 만나면 뒤로 가라
    if arr[x][y] == 0:
        return



    # 방문했다고 남겨주기
    visited[x][y] = True
    result_x.append(x)
    result_y.append(y)


        
    for ndir in (direction, (direction+1)%4):
        nx = x + dx[ndir]
        ny = x + dy[ndir]









# 사각형 갯수 선언 각 인덱스가 사각형 크기인 거임.
# 여기서 하나씩 뺴갈 건데, 하나라도 -1이 된다면 return -1
rectangle = [0,5,5,5,5,5]
visited = [[0]*10 for _ in range(10)]
arr = [list(map(int, input().split())) for _ in range(10)]

for i in range()


find_cnt()

result 

