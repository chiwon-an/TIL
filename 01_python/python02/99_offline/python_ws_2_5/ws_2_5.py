# 문제
# 영화관 시스템을 확장하여 상속을 활용한 클래스를 정의하시오. 부모 클래스와 자식 클래스의 개념을 활용하여 영화관의 기본 정보를 설정하고, 영화관의 상태를 관리하는 메서드를 구현하시오.
# ※ 이전에 작성한 코드를 참고하지 말고, 처음부터 다시 작성한다.
# 요구사항
# 'Theater' 부모 클래스를 정의한다.
    # 'Theater' 클래스는 영화관의 이름을 저장하는 'name' 인스턴스 변수를 가진다.
    # 'Theater' 클래스는 영화관의 총 좌석 수를 저장하는 'total_seats' 인스턴스 변수를 가진다.
    # 'Theater' 클래스는 현재 예약된 좌석 수를 저장하는 'reserved_seats' 인스턴스 변수를 가진다.    
    # 'Theater' 클래스는 좌석을 예약하는 'reserve_seat' 인스턴스 메서드를 가진다.
        # 'reserve_seat' 메서드는 예약 가능한 좌석이 있는 경우, 'reserved_seats'를 1 증가시키고 예약 성공 메시지를 반환한다.
        # 예약 가능한 좌석이 없는 경우, 예약 실패 메시지를 반환한다.

# MovieTheater 자식 클래스를 정의하고, Theater 클래스를 상속받는다.
    # MovieTheater 클래스는 영화관의 총 영화 수를 저장하는 total_movies 클래스 변수를 가진다.
    # MovieTheater 클래스는 영화관의 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다.
        # add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
    # MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
        # description 메서드는 영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 출력한다.


# 아래에 코드를 작성하시오.


class Theater:

    # 'Theater' 클래스는 영화관의 이름을 저장하는 'name' 인스턴스 변수를 가진다.
    # 'Theater' 클래스는 영화관의 총 좌석 수를 저장하는 'total_seats' 인스턴스 변수를 가진다.
    # 'Theater' 클래스는 현재 예약된 좌석 수를 저장하는 'reserved_seats' 인스턴스 변수를 가진다.    

    def __init__(self, name, total_seats, reserved_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = reserved_seats

    # 'Theater' 클래스는 좌석을 예약하는 'reserve_seat' 인스턴스 메서드를 가진다.
        # 'reserve_seat' 메서드는 예약 가능한 좌석이 있는 경우, 'reserved_seats'를 1 증가시키고 예약 성공 메시지를 반환한다.
        # 예약 가능한 좌석이 없는 경우, 예약 실패 메시지를 반환한다.

    def reserve_seat(self):
        if self.reserved_seats >= self.total_seats:
            return '예약이 불가합니다.'
        else :
            self.reserved_seats += 1
            return '좌석 예약이 완료되었습니다.'


# MovieTheater 자식 클래스를 정의하고, Theater 클래스를 상속받는다.

class MovieTheater(Theater):
    # MovieTheater 클래스는 영화관의 총 영화 수를 저장하는 total_movies 클래스 변수를 가진다.

    total_movies = 0

    def __init__(self, name, total_seats, reserved_seats):
        super().__init__(name, total_seats, reserved_seats)
    
    # MovieTheater 클래스는 영화관의 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다.
        # add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.

    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return '영화 추가 성공'
    
    # MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
        # description 메서드는 영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 출력한다.

    @staticmethod
    def description():
        print(f'영화관 이름: {MovieTheater.self.name}')
        print(f'총 좌석 수: {MovieTheater.self.total_seats}')
        print(f'예약된 좌석 수: {MovieTheater.self.reserved_seats}')
        print(f'총 영화 수: {MovieTheater.total_movies}')

# 인스턴스 생성
mega = MovieTheater('메가박스', 10, 0)

#영화 예약
print(mega.reserve_seat())
print(mega.reserve_seat())

#정보 출력
mega.description()