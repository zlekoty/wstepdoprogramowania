import math
class Rocket:
    def __init__(self,a=0,b=0,v=0,s=[]):
        self.x=a
        self.y=b
        self.v=v
        self.s=[]
    def __str__(self):
        return f"({self.x},{self.y})"
    def move(self,x,y):
        self.x=self.x+x
        self.y=self.y+y
        z=math.sqrt(x**2+y**2)
        self.s.append(z)
    def get_position(self):
        return (self.x, self.y)
    def get_distance(self,Rocket2):
        return 'odległość', m.sqrt((self.x-Rocket2.x)**2+(self.y-Rocket2.y)**2)
    def droga(self):
        d=0
        for i in range(len(self.s)):
            d=d+self.s[i]
        return d
