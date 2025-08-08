'''
3개를 뽑아 -> 순서 상관 없으므로 combination
이게 트리플이나 런? -> count += 1
나머지에도 그런게 있나? -> 탐색
count == 2
'''


import sys
sys.stdin = open('input (1).txt','r')

T = int(input())

for tc in range(1,T+1):
    cards = map