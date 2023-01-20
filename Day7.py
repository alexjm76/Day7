#Generator: Yeild 는 함수가 멈추지 않고 계속 실행된다. 장단점 : generator는 메모리 절약 가능, 저장을 안함(last 값만 기억하고 나머지는 버린다.
#단점: 잠깐 실행되느 마는 느낌이라 메모리 저장이 안됨
#상속의 장점 : 코드의 중복을 피할 수 있다.

#override는 부모 클라스에서 정의된 함수를 가져와서 다시 정의하는 것을 의미한다.

class Person():
    def __init__(self,name):
        self.name = name

class MDPerson(Person):
    def __init__(self,name):
        self.name = "Doctor" + name

class JDPerson(Person):
    def __init__(self,name):
        self.name=name + ", Esquire"