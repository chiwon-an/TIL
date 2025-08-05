import sys

sys.stdin = open('input.txt' , 'r')

def dfs(ori,ch_num):
    global max_num
    if ch_num == change:
        max_num = max(int(ori),max_num)
        return

    if (ori,ch_num) in visited:
        return
    visited.add((ori, ch_num))


    ori = list(ori)
    for i in range(len(ori)):
        for j in range(i+1,len(ori)):
                ori[i],ori[j] = ori[j],ori[i]
                dfs(''.join(ori), ch_num + 1)
                ori[i], ori[j] = ori[j], ori[i]
                

test = int(input())
for tc in range(1, test + 1):
    origin, change = input().split()
    change = int(change)
    max_num = 0
    visited = set()
    dfs(origin, 0)
    print(f"#{tc} {max_num}") 