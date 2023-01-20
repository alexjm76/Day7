class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse): #먼저 써있는 동키에 가고 없으면 horse으로 가고 거기도 없으면 animal로 간다.
    pass

class Hinny(Horse, Donkey):
    # def says(self):
    #     return "Hinny cries"
    pass

m1 = Mule()
h1 = Hinny()
print(m1.says())
print(h1.says())

print(Mule.mro()) #순서 확인용 Mule -> Donkey -> Horse -> Animal