import sys
sys.stdin = open('sample_input.txt','r') 

# 좌상, 좌하, 우하, 우상
dx = [-1, 1, 1, -1]
dy = [-1, -1, 1, 1]

def find_optimal_route(x,y, direction, result, turned): 
     
    global max_result, nx, ny
    
    # 범위 벗어나는 건 안 돼 !
    if 0 > x or x > N-1 or 0 > y or y > N-1:
        return
    
    # 종료 조건(처음 위치랑 같아지면 종료! 라는 조건을 쓸 수가 있나?) 
    if x == sx and y == sy and turned == 3 and len(result) >= 4:
        max_result = max(max_result, len(result))
        return max_result
    
    # 방문한 적이 있는 곳은 안 돼 (처음에는 방문한 곳이 있잖아.)
    if visited[x][y]:
        return 
    
    # 같은 종류의 디저트 카페를 만나면 안 됨. 근데 이러면 시작조건이랑 똑같아짐.
    if cafes[x][y] in result:
        return
        
    # 현재 좌표에서 해야할 일
    visited[x][y] = True
    result.append(cafes[x][y])
    
    # 다음꺼 드가자 = 현재 방향 유지 or 다음 방향(회전)만 허용    
    
    # 방향은 지금 방향 유지 OR 다음 방향 2가지 선택밖에 없음.
    for ndir in (direction, (direction+1) % 4):
        
        nx = x + dx[ndir]
        ny = y + dy[ndir]
        
        # 3번 돌아야 사각형이 완성됨. 방향이 바꼈다면, turned에  + 1
        if ndir != direction:
            turned += 1
        
        # 회전은 최대 3번
        if turned <= 3:
            find_optimal_route(nx, ny, ndir, result, turned)

    # 되돌리기
    result.pop()
    visited[x][y] = False
        
        
T = int(input())        
        
for tc in range(1, T+1):
    N = int(input()) 
    cafes = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]* N for _ in range(N)]
    max_result = -1
    result = []
    
    # 방향에 따른 시작좌표 계산 후 하나씩 넣어주기
    for sx in range(1,N-1):
        for sy in range(1,N):
            find_optimal_route(sx,sy, 0, result, 0)
    
    print(f'#{tc} {max_result}')