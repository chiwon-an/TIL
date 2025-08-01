import sys
sys.stdin = open('sample_input.txt', 'r')

class Stack:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.item = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity -1

    def push(self, item):

        if self.is_full(): # True라면 값을 삽입할 수 없음.
            print('Stack is Full!!!')

        self.top += 1   # 올바른 삽입 위치 찾기
        self.item[self.top] = item

    def pop(self):
        if self.is_empty():
            print('Stack is Empty!!')
            return
        item = self.item[self.top]
        self.item[self.top] = None
        self.top -= 1
        return item     # 제거한 값을 반환



T = int(input())

for tc in range(1, T+1):
    a = list(input())
    stack = Stack()

    for item in a:
        stack.push(item)

        if

