class PrettyMixin:
    def time_print(self):
        import datetime
        print(datetime.date.today())


    def dump(self):
        import pprint
        pprint.pprint(vars(self)) #dictionary로 저장하는 변수 vars

class Thing(PrettyMixin):
    pass

t = Thing()
t.time_print()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.gender = "female"
t.gender = "male"  #이걸로 덮어짐
t.dump()
#{'age': 'eldritch', 'feature': 'ichor', 'name': 'Nyarlathotep'}