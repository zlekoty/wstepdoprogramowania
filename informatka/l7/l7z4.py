import math
class Rocket:
    def __init__(self,a=0,b=0,v=0,m=0):
        self.x=a
        self.y=b
        self.m=m
        self.v=v
    def __str__(self):
        return f"({self.x},{self.y})"
    def move(self,x,y):
        self.x=self.x+x
        self.y=self.y+y
    def get_position(self):
        return (self.x, self.y)
    def get_distance(self,Rocket2):
        return 'odległość', m.sqrt((self.x-Rocket2.x)**2+(self.y-Rocket2.y)**2)
    def promień(self):
        return math.sqrt((self.x)**2+(self.y)**2)
    def ziemia(self):
        
