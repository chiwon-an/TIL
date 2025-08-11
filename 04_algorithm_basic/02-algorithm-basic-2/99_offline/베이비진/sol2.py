import sys
from itertools import combinations
sys.stdin = open('input (1).txt', 'r')

'''

6장의 카드를 받는다. 

6장의 카드를 받으면, 이 6장이 연속 3장(RUN) / 같은 거 3장(triple)인지 판단을 해줘야 한다.

3장의 조합을 찾고, 찾았다 ! -> 나머지 3장도 그게 되는지 확인해주면 되는 거 아님?

그러면 이렇게 dfs로 접근 가능한 거 아님?

'''
def run_triple(mixture):
    a = []
    for i in mixture:
        a.append(i)

    if sorted(a) == list(range(min(a), min(a)+3)):
        return True
    
    if len(set(a)) == 1:
        return True
    
    else: return False

# def triple(mixture):
#     if a == b == c:
#         return True
#     else: return False



def baby_jin(cards):

    # 탈출 조건

    if len(cards) == 0:
        return 'true'

    
    # 3장을 뽑기
    comb = list(combinations(cards, 3))

    for item in comb:
        if run_triple(item) == True:
            temp_cards = cards[:]
            for card in item:
                temp_cards.remove(card)
            
            return baby_jin(temp_cards)

    return 'false'


T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input()))
    a = list(combinations(cards, 3))

    print(f'#{tc} {baby_jin(cards)}')