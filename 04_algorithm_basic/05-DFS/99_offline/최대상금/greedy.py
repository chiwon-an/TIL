import sys
sys.stdin = open('input.txt','r')

'''
제일 큰 숫자를 찾아서 맨 앞부터 순서대로 바꾸기 (인덱스가 중요)

조건

제일 커진 숫자를 구할 수 있잖아. 그거랑 같아지고, 짝수번 남았으면 그냥 그거 출력 / 홀수번 남았으면 맨 뒤에서 한 번 바꾸기


'''

T = int(input())

for tc in range(1, T+1):
    
    # str형태로 입력 받기
    number, change = map(str, input().split())
    
    lst = []
    
    # number의 각 숫자를 큰 숫자대로 리스트에 넣어주기
    for item in number:
        lst.append(int(item))
    
    target = lst[:]
    
    # target에 각 자리수를 내림차순으로 정리해두기(제일 큰 숫자임)
    target.sort(reverse=True)
    
    for iter in range(int(change)):
        
        # 만약 이미 최대값에 도달했으면, 반복이 몇 번 남았는지가 중요
        if lst == target:
            remain = int(change) - iter
            if remain % 2 == 1:
                # 모든 숫자가 다르면 마지막 두 자리를 바꿔야 함
                if len(set(lst)) == len(lst):
                    lst[-1], lst[-2] = lst[-2], lst[-1]
                break
            else:
                break
                
            
            
            
        
        # iter이 주어진 number보다 길면 인덱스 에러가 남.
        if iter < len(lst)-1:
            # idx = lst.index(target[iter])
            idx = len(lst) - 1 - lst[::-1].index(target[iter])
            if iter != idx:
                lst[iter], lst[idx] = lst[idx], lst[iter]
            
            else:
                idx = len(lst) - 1 - lst[::-1].index(target[iter+1])
                # idx = lst.index(target[iter+1])
                lst[iter], lst[idx] = lst[idx], lst[iter]

           
    
    print(f"#{tc} {''.join(map(str, lst))}")
    