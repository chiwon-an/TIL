import sys
sys.stdin = open('input (1).txt','r')

'''
0~9 사이의 숫자 카드에서 임의의 카드 6 장을 뽑았을 때 ,
3 장의 카드가 연속적인 번호를 갖는 경우를 run 이라 하고 ,
3 장의 카드가 동일한 번호를 갖는 경우를 triplet 이라고 한다

그리고 , 6 장의 카드가 run 과 triplet 로만 구성된 경우를 baby gin 으로 부른다

6 자리의 숫자를 입력 받아 baby gin 여부를 판단하는 프로그램을 작성하라

6장의 카드가 주어짐.
'''
# 베이비진이 되는 경우
    # 모두가 트리플
    # 모두가 런
    # 섞어서( 3 + 3 / )


def judge(card):
    for i in card[:5]:
        for j in card[i+1:6]:
            for k in card[j+1:7]:
                i,j,k = int(i, j ,k)

                
                if i == j and i == k:
                    card.pop(i)
                    card.pop(j)
                    card.pop(k)
                    count += 1
                
                elif 
    
    if count == 2:
        return True
    else:
        return False

count = 0 # 같은 게 있을 때 몇 개 나왔는지 세기

T = int(input())

for tc in range(1, T+1):
    card = input()
    result = judge(card)


    print(f'#{tc} {result}')