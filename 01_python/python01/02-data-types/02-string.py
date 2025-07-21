# Hello, World!
print('Hello, World!') 
# str
print(type('Hello, World!')) 


bugs = 'roaches'
counts = 13
area = 'living room'
# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')


my_str = 'hello'
# 인덱싱
print(my_str[1]) # e
# 슬라이싱
print(my_str[2:4]) # ll
# 길이
print(len(my_str)) # 5

# TypeError: 'str' object does not support item assignment
# my_str[1] = 'z'


# replace
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text)  # Hello, Python!
print(text)  # Hello, world! (original string remains unchanged)

# strip (공백이나 특정 문자 제거)
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)  # 'Hello, world!'


# split(',', maxsplit) # (구분자로 문자열을 나누어 리스트로 반환)

text = 'Hello, world, and you!'
words = text.split(',')
words_1 = text.split(',', 1)
print(words)  # ['Hello', ' world!']
print(words_1) # ['Hello', ' world, and you!']

# join(구분자로 iterable의 문자열을 연결한 문자열을 반환)
words = ['Hello', 'world!']
text = '-'.join(words)
print(text)  # 'Hello-world!'
