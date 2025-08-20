'''
수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.

한 조의 인원에 제한 x
한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.

ex) 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다.
    번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

1번부터 N번까지의 출석번호가 있고, 
M 장의 신청서가 제출되었을 때 전체 몇 개의 조가 만들어지는지 출력하는 프로그램을 만드시오.

리스트 안의 리스트로 넣어주기 만약에 하나라도
[1,2]
[3,4]
이런 식으로 만들어주고, 기존에 만들어진 리스트 안에 값이 있다면 거기 안에 써주고,
만약 두 값이 다른 리스트에 있다면? -> 그 두 리스트를 합치기
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    
    N, M = map(int, input().split())

    lst = list(map(int, input().split()))
    # print(lst)

    relationships = []
    for i in range(0, len(lst), 2):
        relationships.append(lst[i:i+2])

    # print(relationships)
    result = []
    
    for relationship in relationships:
        
        if len(result) == 0:
            result.append(relationship)
        
        for length in range(len(result)):
                          
            if relationship[0] in result[length]:

                result[length] += relationship
            
            if relationship[1] in result[length]:

                result[length] += relationship

            else:
                result.append(relationship)
    
    real_result = []
    for item in result:
        real_result.append(set(item))

    print(real_result)
    
    # 1~N까지 돌면서 자기가 속한 집합이 있는지 확인해보고, 두 개 이상인 경우 그 두 개를 합하기.
    # 하나도 없으면 자기만 속한 집합 생성

    for i in range(N):
        cnt = 0
        idx_lst = []
        idx = - 1
        
        for item in result:
            idx += 1
        
            if i in item:
                cnt += 1
                idx_lst.append((i, idx))
        
        if cnt == 0:
            real_result.append(set(i))
        
        elif cnt == 1:
            continue
            
        elif cnt >= 2:
            real_result[]




