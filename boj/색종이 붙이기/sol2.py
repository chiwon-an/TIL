'''
1. 맨 왼쪽 위에서 1인 걸 찾기
2. 5-> 1로 가능한 것 판단
3. 
'''

def find_cnt(x,y,s):

    if s == 1:
        if rectangle[1] >= 1:
            rectangle[1] -= 1
            arr[x][y] = 0
            return -1
        
        elif rectangle[1] == 0:
            return
    
    if x + s >= 10 or y + s >= 10:
        find_cnt(x,y,s-1)


    for i in range(x, x+s):
        for j in range(y, y+s):
        
            if arr[i][j] == 0:
                find_cnt(x,y,s-1)
    
    if rectangle[s] >= 1:
        rectangle[s] -= 1
        for i in range(x, x+s):
            for j in range(y, y+s):
                arr[i][j] = 0
        
        return


    elif rectangle[s] == 0:
        find_cnt(x,y,s-1)




arr = [list(map(int, input().split())) for _ in range(10)]

max_ans = float('inf')

rectangle = [0,5,5,5,5,5]
temp = [[0]*5 for _ in range(5)]

for x in range(10):
    for y in range(10):

        if arr[x][y] == 1:
            print(find_cnt(x,y,5))

