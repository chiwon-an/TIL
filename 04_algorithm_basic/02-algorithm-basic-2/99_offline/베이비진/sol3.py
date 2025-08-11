import sys
sys.stdin = open('input (1).txt', 'r')

# def run_triple(mixture):
#     a = []
#     for i in mixture:
#         a.append(i)

#     if sorted(a) == list(range(min(a), min(a)+3)):
#         return True
    
#     if len(set(a)) == 1:
#         return True
    
#     else: return False


# def baby_jin(cards):

#     # 탈출 조건

#     if len(cards) == 0:
#         return 'true'

    
#     # 3장을 뽑기
#     comb = list(combinations(cards, 3))

#     for item in comb:
#         if run_triple(item) == True:
#             temp_cards = cards[:]
#             for card in item:
#                 temp_cards.remove(card)
            
#             return baby_jin(temp_cards)

#     return 'false'

def baby_gin(cnt_lst):

    if sum(cnt_lst) == 0:
        return 'true'

    for i in range(10):
        if cnt_lst[i] == 6:
            return 'true'
        
        if cnt_lst[i] >= 3:
            cnt_lst[i] -= 3

            # if baby_gin(cnt_lst):
            #     return True
            
            # cnt_lst[i] += 3  # 백트래킹

    for i in range(8):
        if cnt_lst[i] >= 1 and cnt_lst[i+1] >= 1 and cnt_lst[i+2] >= 1:
            cnt_lst[i]  -= 1
            cnt_lst[i+1] -= 1 
            cnt_lst[i+2] -= 1
            return baby_gin(cnt_lst)
    
    return 'false'

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input()))
    cnt_lst = [0]*10

    # print(cards)
    for card in cards:
        cnt_lst[card] += 1
    
    # print(cnt_lst)

    print(f'#{tc} {baby_gin(cnt_lst)}')

    