# 문제
# 영화관 시스템을 모델링하는 클래스를 정의하시오. 클래스와 객체의 개념을 활용하여 영화관의 기본 정보를 설정하고, 영화관의 상태를 관리하는 메서드를 구현하시오.
# 요구사항
# 3433번 문제에서 작성한 코드에서 이어서 작성한다.


# MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
    # description 메서드는 아래 문장을 출력한다.
# '"이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다."
# "영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다."

# 아래에 코드를 작성하시오.

class MovieTheater:
    # MovieTheater 클래스는 모든 영화관이 공통으로 가지는 total_movies변수를 가진다.
        # total_movies 변수를 MovieTheater 클래스에 클래스 변수로 추가한다.
    total_movies = 0
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0

    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return "좌석 예약이 완료되었습니다."
        else:
            return "더 이상 예약 가능한 좌석이 없습니다."

    def current_status(self):
        print(f"총 좌석 수: {self.total_seats}")
        print(f"예약된 좌석 수: {self.reserved_seats}")

    # MovieTheater 클래스는 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다
    # add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        print('영화 추가 성공')

    @staticmethod
    def description():
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.")
        print("영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")

class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats
        self.reserved_vip_seats = 0
    
    def reserve_vip_seat(self):
        if self.reserved_vip_seats < self.vip_seats:
            self.reserved_vip_seats += 1
            return 'VIP좌석 예약이 완료되었습니다.'

        else :
            return '예약 가능한 VIP 좌석이 없습니다.'

    def reserve_seat(self):
        if self.reserved_vip_seats < self.vip_seats:
            return self.reserve_vip_seat()
        else:
            return super().reserve_seat()


# 테스트용 인스턴스 생성 및 출력
mega = MovieTheater("메가박스", 100)
cgv = MovieTheater("CGV", 150)

# 좌석 예약
print(mega.reserve_seat())
print(mega.reserve_seat())
print(mega.reserve_seat())

# 영화 추가
MovieTheater.add_movie()
MovieTheater.add_movie()

# 상태 출력
mega.current_status()
cgv.reserve_seat()
cgv.current_status()

# 총 영화 수 출력
print(f"총 영화 수: {MovieTheater.total_movies}")

# 설명 출력
MovieTheater.description()