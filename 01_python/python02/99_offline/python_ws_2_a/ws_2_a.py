# 파이썬의 class를 연습하고자 한다. 'SNS 사용자'의 특성을 가진 class를 요구 사항에 맞춰 정의하시오.
# 요구사항
# User 클래스를 정의한다.
# User의 인스턴스 수를 기록할 수 있는 클래스 변수 user_count를 정의하고, 0을 할당한다.
# 생성자 메서드를 정의한다.
# 생성자 메서드는 사용자의 이름과 이메일을 인자로 받는다.
# 각 인스턴스는 고유한 이름과 이메일을 담을 수 있는 name과 email 변수를 가지고, 인자로 넘겨받은 값을 할당 받는다.
# 인스턴스가 생성될 때마다 user_count가 1 증가해야 한다.
# 'SNS 사용자'에 대한 설명을 출력하는 description 스태틱 메서드를 정의한다.
# 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 name과 email을 출력한다.
# User 클래스의 user_count를 출력한다.
# description 스태틱 메서드를 호출한다.

# 아래에 코드를 작성하시오.

class User:

    # User의 인스턴스 수를 기록할 수 있는 클래스 변수 user_count를 정의하고, 0을 할당한다.
    user_acount = 0

    # 생성자 메서드를 정의한다.  
    def __init__(self, name, email):

        # 생성자 메서드는 사용자의 이름과 이메일을 인자로 받는다.
        # 각 인스턴스는 고유한 이름과 이메일을 담을 수 있는 name과 email 변수를 가지고, 인자로 넘겨받은 값을 할당 받는다.
        self.name = name
        self.email = email

        # 인스턴스가 생성될 때마다 user_count가 1 증가해야 한다.
        User.user_acount += 1

    def __str__(self):
        return f'이름: {self.name}, 이메일: {self.email}'

    @staticmethod
    def description():
        return print("SNS 사용자: 이름과 이메일을 가지고 있습니다.")

    

# 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 name과 email을 출력한다.
sample1 = User('Alice', 'alice@example.com')
sample2 = User('Bob', 'bob@example.com')

print(sample1)
print(sample2)
print(f'현재까지 생성된 사용자 수 :{User.user_acount}')

# description 스태틱 메서드를 호출한다.
User.description()
