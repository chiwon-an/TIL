# # 아래에 코드를 작성하시오.
# 문제
# 파이썬의 조건문과 반복문을 연습하고자 한다. 요구사항을 만족하는 코드를 작성하시오.
# 요구사항
# numbers 리스트에 1부터 10까지의 정수를 할당한다.
# numbers 리스트의 각 요소를 순회하며, 짝수일 경우 해당 숫자를 출력한다.
# numbers 리스트의 각 요소를 순회하며, 홀수일 경우 해당 숫자를 '홀수'로 출력한다.
# numbers 리스트의 각 요소를 순회하며, 숫자가 5일 경우 반복을 종료한다.

numbers = []
for i in range(1, 11):
    numbers.append(i)

for i in range(len(numbers)):

    if numbers[i] % 2 == 0:
        print(numbers[i])
    
    elif numbers[i] == 5:
        break
    
    else :
        print(f'{numbers[i]}은(는) 홀수')
