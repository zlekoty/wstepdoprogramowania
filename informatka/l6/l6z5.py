import dyski as  d
import random as r
import math as m
lista=[]
for i in range (0,100):
    dysk=d.dysk(r.uniform(-15,15),r.uniform(-15,15),0.5)
    lista.append(dysk)
    print(i,dysk)
for i in range(0,99):
    for j in range(1,100):
        while d.kolizja(lista[i],lista[j]) is True:
            print(i,j)
            if lista[j].x>=0:
                a=r.uniform(-15-lista[j].x,15-lista[j].x)
            if lista[j].x<0:
                a=r.uniform(-15+lista[j].x,15-lista[j].x)
            if lista[j].y>=0:
                b=r.uniform(-15-lista[j].y,15-lista[j].y)
            if lista[j].y<0:
                b=r.uniform(-15+lista[j].y,15-lista[j].y)
            v=[a,b]
            lista[j].przesun(v)

            
        
