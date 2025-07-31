import sys
sys.stdin = open("sample_input.txt", 'r')

T = int(input())

for tc in range(1, T+1):
    count = 0
    now = K
    charge = 0
    while now < N :
        if station[now] == 1:
            count += 1
            charge = now
            now += K
        else:
            now -= 1
