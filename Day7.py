# class

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성 : ", end=" ")

    def info(self):
        print(f"{self.owner}의 포켓몬은 입니다")
        for skill in self.skills:
            print(skill)

    def attack(self, idx):  #공격하는 클래스
        print(f"{self.skills[idx]} 공격 시전!")


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills) #부모 클래스 호출
        print(f"피카츄")

class Ggoboogi(Pokemon): #inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills) #부모 클래스를 상속 받는 함수 owner,skills 상속 받음
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):  #공격하는 클래스
        print(f"{self.owner}의  {self.name} 가 {self.skills[idx]} 공격 시전!")

    def swim(self):
        print(f"{self.name}가 수영을 합니다.")


pk1 = Pikachu('한지우', '번개/백만볼트')
pk1.info()
ggo1 = Ggoboogi("오바람", "고속스핀/거품/몸통박치기")
ggo1.info()
ggo1.attack(2)
ggo1.swim()
# p1 = Pokemon( '한지우', '50만 볼트/100만 볼트/번개')
# p2 = Pokemon( '오바람', '고속스핀/거품/몸통박치기/하이드로펌프')
