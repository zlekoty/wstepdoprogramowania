import math as m
class punkt:
    """Reprezentuje punkt w przestrzeni dwuwymiarowej.

    atrybuty: x,y"""
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    def __str__(self):
        """Wypisuje wspolrzedne punktu"""
        return f"({self.x},{self.y})"
    def przesun(self,v):
        """Przesuwa punkt o podany wektor v """
        a=v[0]
        b=v[1]
        self.x=self.x+a
        self.y=self.y+b
class dysk(punkt):
    """Reprezentuje punkt w przestrzeni dwuwymiarowej.

    atrybuty: x,y,r"""
    def __init__(self,x=0.0,y=0.0,r=0):
        punkt.__init__(self,x,y)
        self.r=r
    def __str__(self):
        """Wypisuje wspolrzedne dysku i promień"""
        return f"({self.x},{self.y},{self.r})"
    def przesun(self,v):
        """Przesuwa dysk o podany wektor v """
        a=v[0]
        b=v[1]
        self.x=self.x+a
        self.y=self.y+b
def odl(p1,p2):
    """oblicza odległość między dwoma punktami"""
    x1=m.fabs(p1.x-p2.x)
    y1=m.fabs(p1.y-p2.y)
    o=m.sqrt(x1**2+y1**2)
    return o
def kolizja(d1,d2):
    """wykrywa kolizję między zadanymi dyskami"""
    o=odl(d1,d2)
    if m.fabs(d1.r-d2.r)<o<m.fabs(d1.r+d2.r):
        return True
    else:
        return False
