'''
동물의 특성을 가진 클래스를 상속과 다형성을 활용하여 구현하시오.
요구사항
Animal 클래스를 정의한다.
    Animal 클래스는 이름을 인자로 받는 생성자 메서드를 가진다.
    Animal 클래스는 speak 메서드를 가진다. 이 메서드는 자식 클래스에서 오버라이딩된다.
Dog와 Cat 클래스를 정의하고, Animal 클래스를 상속받는다.
    Dog 클래스는 speak 메서드를 오버라이딩하여 "Woof!"를 반환한다.
    Cat 클래스는 speak 메서드를 오버라이딩하여 "Meow!"를 반환한다.
Flyer와 Swimmer 클래스를 정의한다.
    Flyer 클래스는 fly 메서드를 가진다. 이 메서드는 "Flying"을 반환한다.
    Swimmer 클래스는 swim 메서드를 가진다. 이 메서드는 "Swimming"을 반환한다.
Duck 클래스를 정의하고, Flyer와 Swimmer 클래스를 다중 상속받는다.
    Duck 클래스는 Animal 클래스를 상속받고, 이름을 인자로 받는 생성자 메서드를 가진다.
    Duck 클래스는 speak 메서드를 오버라이딩하여 "Quack!"을 반환한다.
make_animal_speak 함수를 정의한다.
    이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
코드를 실행하고, 출력 결과를 확인한다.
'''

class Animal:
    # Animal 클래스는 이름을 인자로 받는 생성자 메서드를 가진다.
    def __init__(self, name):
        self.name = name
    
    # Animal 클래스는 speak 메서드를 가진다. 이 메서드는 자식 클래스에서 오버라이딩된다.
    # 아무런 기능도 없는 메서드를 왜 정의할까?
    '''
        나중에 만들 클래스들이 상속 받아서 각각의 메서드를 가지게 될텐데, 왜 굳이 정의할까?
        하위 클래스들이 모두 공통적으로 speak 메서드를 가지고 있을 것이다 라는 사실을 명시
        animal class를 상속받을 자식 클래스들이 모두 speak 메서드를 각자의 역할로써 정의하고 있다.
    '''
    def speak():
        pass        

class Dog(Animal):      # 본인이 사용할 모양으로 오버라이딩해서 사용하고 있다.
    def speak(self):
        return 'Woof!'
    
class Cat(Animal):
    def speak(self):
        return 'Mewo!'

class Flyer:
    def fly(self):
        return "Flying"
    
class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer, Animal):
    def speak(self):
        return "Quack!"

'''
make_animal_speak 함수를 정의한다.
이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
'''
def make_animal_speak(instance):
    print(instance.speak())

d1 = Dog('치와와')
c1 = Cat('페르시안 블루')
duck_1 = Duck('거위')

make_animal_speak(d1)
make_animal_speak(c1)
make_animal_speak(duck_1)