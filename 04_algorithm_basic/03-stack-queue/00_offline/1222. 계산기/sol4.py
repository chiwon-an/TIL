import sys
sys.stdin = open('input.txt','r')

def to_postfix(expression):

    # 연산자를 임시로 담아둘 곳
    stack = []

    # 여기는 후위표현식
    postfix = []


    for char in expression:
        
        # 들어올 차례인 것이 숫자라면?
        if char.isnumeric():

            # 바로 표현식에다가 넣어도 무방
            postfix.append(char)
        
        # 근데 만약 숫자가 아니라면?
        else:

            # 스택이 비어있는지부터 확인. 스택에 뭐가 있어 !
            if stack:

                # 스택에서 pop을 해주고 그걸 표현식에 넣기
                postfix.append(stack.pop())

            # 이번에 받은 연산자는 stack에 담아두기
            stack.append(char)
        
    # stack에 남은 것들이 있다면? -> 후위식에 넣어두기 ! (짬처리)
    while stack:
        postfix.append(stack.pop())
        
    return postfix


def calculate(postfix):

    stack = []
    temp = []

    for i in postfix:

        if i.isnumeric():
            stack.append(i)
        
        elif i == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a+b)
    
    return stack.pop()

for tc in range(1,11):
    N = int(input())

    # 여기선 후위표현식으로 바꿔주는 것까지 !
    postfix = to_postfix(input())

    # 계산을 해줄 차례
    result = calculate(postfix)

    print(f'#{tc} {result}')