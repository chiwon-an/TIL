import sys
sys.stdin = open('input.txt','r')

def infix_to_postfix(expression):
    # 연산자의 우선 순위를 정의
    op = {'+' : 1,'-' : 1, '*': 2, '/': 2 ,'(' : 0}
    stack = []  # 연산자를 저장할 스택
    postfix = []    # 후위 표기식을 저장할 리스트

    for chat in expression:


T = int(input())

for tc in range(1, T+1):
