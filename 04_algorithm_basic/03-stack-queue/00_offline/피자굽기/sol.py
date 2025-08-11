import sys
from collections import deque
sys.stdin = open('sample_input (1).txt', 'r')

'''
N개의 피자를 굽는 화덕 -> 치즈가 다 녹아야 꺼냄 -> 
피자마다 치즈 양이 다름 -> 

1의 자리에 왔을 때 피자를 꺼낼 수 있음. -> 한 바퀴 돌 때마다 남은 치즈의 1/2이 녹음

피자를 구울 수 있는 것보다 피자가 많음 따라서 다 구운 것들은 빼줘야함. -> 약간 선입선출 구조 아닌가? -> 큐 아님?

마지막 번호를 가져오는게 쉽지가 않을 것 같음...
'''

def rotation(pizza):
    
    while len(pizza) > 1:

        if pizza[0][1] == 0:
            pizza.popleft()

            if spare:
                next = spare.popleft()
                pizza.appendleft(next)

        else:
            a = (pizza[0][0], pizza[0][1]//2)
            pizza.popleft()
            pizza.append(a)
    
    return pizza

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    pizza = []
    for i in range(N):
        pizza.append((i+1, cheese[i]))
    pizza = deque(pizza)

    spare = []
    for i in range(N, M):
        spare.append((i+1, cheese[i]))

    spare = deque(spare)

    print(f'#{tc} {rotation(pizza)[0][0]}')