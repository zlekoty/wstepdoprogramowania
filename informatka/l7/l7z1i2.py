import math as m
class Rocket:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b
    def __str__(self):
        return f"({self.x},{self.y})"
    def move(self,x,y):
        self.x=self.x+x
        self.y=self.y+y
    def get_position(self):
        return (self.x, self.y)
    def get_distance(self,Rocket2):
        return 'odległość', m.sqrt((self.x-Rocket2.x)**2+(self.y-Rocket2.y)**2)
'''r=Rocket()
print('r',r.get_position())
r.move(10,32)
print('r',r.get_position())
r.move(-50,18)
print('r',r.get_position())
r.move(40,-50)
print('r',r.get_position())'''
