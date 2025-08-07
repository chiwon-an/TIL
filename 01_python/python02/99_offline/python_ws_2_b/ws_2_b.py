# 파이썬의 class를 연습하고자 한다. 'SNS 게시물'의 특성을 가진 class를 요구 사항에 맞춰 정의하시오.
# 요구사항
# Post 클래스를 정의한다.
# Post의 인스턴스 수를 기록할 수 있는 클래스 변수 post_count를 정의하고, 0을 할당한다.
# 생성자 메서드를 정의한다.
# 생성자 메서드는 게시물의 제목과 내용을 인자로 받는다.
# 각 인스턴스는 고유한 제목과 내용을 담을 수 있는 title과 content 변수를 가지고, 인자로 넘겨받은 값을 할당 받는다.
# 인스턴스가 생성될 때마다 post_count가 1 증가해야 한다.
# 게시물의 내용을 출력하는 show_content 인스턴스 메서드를 정의한다.
# 게시물의 총 개수를 출력하는 total_posts 클래스 메서드를 정의한다.
# 'SNS 게시물'에 대한 설명을 출력하는 description 정적 메서드를 정의한다.
# 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 title과 content를 출력한다.
# Post 클래스의 total_posts 클래스 메서드를 호출하여 게시물의 총 개수를 출력한다.
# description 정적 메서드를 호출한다.


# 아래에 코드를 작성하시오.

# Post 클래스를 정의한다.
class Post:

    # Post의 인스턴스 수를 기록할 수 있는 클래스 변수 post_count를 정의하고, 0을 할당한다.
    post_count = 0

    # 생성자 메서드를 정의한다.
    # 생성자 메서드는 게시물의 제목과 내용을 인자로 받는다.
    # 각 인스턴스는 고유한 제목과 내용을 담을 수 있는 title과 content 변수를 가지고, 인자로 넘겨받은 값을 할당 받는다.
    # 인스턴스가 생성될 때마다 post_count가 1 증가해야 한다.
    def __init__(self, title, content):
        self.title = title
        self.content = content
        Post.post_count += 1

    # 게시물의 내용을 출력하는 show_content 인스턴스 메서드를 정의한다.
    def show_content(self):
        print(f'Title: {self.title}')
        print(f'Content: {self.content}')
        # return f'Title: {self.content}'
    
    # 게시물의 총 개수를 출력하는 total_posts 클래스 메서드를 정의한다.
    @classmethod
    def total_post(cls):
        print(f'Total posts: {cls.post_count}')
    
    # 'SNS 게시물'에 대한 설명을 출력하는 description 정적 메서드를 정의한다.
    @staticmethod
    def description():
        print('SNS게시물은 소셜 네트워크 서비스에서 사용자가 작성하는 글을  의미합니다.')

# 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 title과 content를 출력한다.
sample_1 = Post('First Post', 'This is the content of First post')
sample_2 = Post('Second Post', 'This is the content of Second post')

sample_1.show_content()
sample_2.show_content()

# Post 클래스의 total_posts 클래스 메서드를 호출하여 게시물의 총 개수를 출력한다.
Post.total_post()

# description 정적 메서드를 호출한다.
Post.description()