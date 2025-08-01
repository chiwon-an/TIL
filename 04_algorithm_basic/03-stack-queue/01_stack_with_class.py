class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity    # 이 자료 구조의 최대 수용 가능 공간
        self.item = [None]*capacity # 내 푀대 크기 만큼 none으로 채운다
        self.top = -1
        # 왜 top이 0이 아니라 -1인가?
        # 여기서 -1은 리스트의 마지막을 의미하는 게 아니라,
        # push연산을 진행할 때, top의 값을 1 증가시키고, 그곳에 값을 삽입

    # 주어진 값을 삽입
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

    def is_full(self):
        # stack이 가득 찼음을 어떻게 알 수 있을까?
        #
        return self.capacity - 1 == self.top

    def is_empty(self):
        return self.top == -1


# stack 자료구조 인스턴스 생성시, 이 자료구조의 최대 크기도 함께 넘겨줘야 한다.
stack = Stack()

print(stack.item)
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
# print(stack.peek())
print(stack.is_empty())
# print(stack.pop())
# print(stack.pop())
