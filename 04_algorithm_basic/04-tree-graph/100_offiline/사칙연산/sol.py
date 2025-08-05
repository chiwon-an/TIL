import sys
sys.stdin = open('input.txt','r')

# 자식 연산자들을 left, right로 받아와.
# 여기서 친절하게 알려주잖아.
# left, right 리스트의 인덱스가 같을 거야.
# 예를 들어, 1-23 이면 left, right의 [1]에 값을 넣어주는 거지.
# 그럼 나중에 1번을 계산할 때 left[1]right[1]을 가져와서 1번에 있는 거에 따라서 하면 되잖아.

def cal(idx):
    if isinstance(tree[idx], int):
        return tree[idx]
    
    left_val = cal(left[idx])
    right_val = cal(right[idx])
            
    # 숫자가 아닐 수도 있으니까 재귀함수 사용        
    if tree[idx] == '+':
        tree[idx] = left_val + right_val
        return tree[idx]
    
    # 숫자가 아닐 수도 있으니까 재귀함수 사용        
    elif tree[idx] == '-':     
        tree[idx] = abs(left_val - right_val)
        return tree[idx]
    
    # 숫자가 아닐 수도 있으니까 재귀함수 사용        
    elif tree[idx] == '*':
        tree[idx] = left_val * right_val
        return tree[idx]
    
    # 숫자가 아닐 수도 있으니까 재귀함수 사용        
    elif tree[idx] == '/':
        tree[idx] = left_val / right_val
        return tree[idx]  
    

# tc가 인풋에 없음.
for tc in range(1,11):

    # N의 값 입력 받기
    N = int(input())

    # 리스트 생성    
    tree = [None]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)
    
    # 입력을 리스트 형태로 받기.
    for _ in range(N):
        user_input = list(map(str, input().split()))

        # 2개의 길이로 들어오면 이건 숫자인 거임.
        if len(user_input) == 2:
            idx = int(user_input[0])
            value = user_input[1]
            tree[idx] = int(value)
        
        # 나머지는 연산자이므로, left[트리의 부모 인덱스] = 자식의 인덱스
        else:
            idx = int(user_input[0])
            value = user_input[1]
            left[idx] = int(user_input[2])
            right[idx] = int(user_input[3])
            tree[idx] = value

            
    result = cal(1)            
    # 최종 출력 형식
    print(f'#{tc} {int(result)}')        
        
                

    