import math


class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def get_area(self):  #instant method
        print("도형의 면적을 출력합니다.")

class Circle(Shape):
    def __init__(self,x,y,radius):
        super().__init__(x,y)
        self.radius = radius

    def get_area(self): #override
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length


    def get_area(self):  # override
        return self.width * self.length


class Cylinder(Circle):
    def __init__(self,x,y,radius, height):
        super().__init__(x,y,radius)
        self.height = height

    def get_area(self): #get volume
        #return math.pi * self.radius * self.radius* self.height
        return super().get_area() * self.height #위에 줄이랑 똑같다.

cy1 = Cylinder(20,20,10,2)
c1 =Circle(100, 100, 10.0)
c2=Circle(50, 50, 2.0)
r1=Rectangle(100, 50, 5,2)
print(f"사각형의 촤표는 x: {r1.x}, y : {r1.y} , 넓이는 {r1.width*r1.length}")
print(c2.get_area())
print(r1.get_area())

#원기둥을 하려면 circle을 상속받으면 편하다.
print(cy1.get_area())