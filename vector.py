import math;
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def norme(self):
        n=math.sqrt(self.x**2 + self.y**2)
        return n
    def somme(self,t):
        self.x+=t.x
        self.y+=t.y
v1=Vector(2,3)
v2=Vector(2,3)
v1.somme(v2)
print(v1.x)
print(v1.y)

