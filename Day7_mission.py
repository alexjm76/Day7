#10.9
class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'


a=Bear()
b=Rabbit()
c=Octothorpe()
print(a.eats())
print(b.eats())
print(c.eats())


#10.10
class Laser():
    def __init__(self):
        self.name = 'disintegrate'
    def does(self):
        return self.name

class Claw():
    def __init__(self):
        self.name = 'crush'
    def does(self):
        return self.name

class SmartPhone():
    def __init__(self):
        self.name = 'ring'
    def does(self):
        return self.name

class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return f"{self.laser.does()}, {self.claw.does()}, {self.smartphone.does()}"

robot = Robot()

print(robot.does())