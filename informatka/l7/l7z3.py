import l7z1i2 as R
import random
flota=[]
for i in range(5):
    flota.append(R.Rocket(random.randint(-50,50),random.randint(-50,50)))
flota2=['r1','r2','r3','r4','r5']
z=0
while z<6:
    for a in range(5):
        for b in range(a+1,5):
            print(flota2[a],flota2[b],flota[a].get_distance(flota[b]))
    
    for i in range(5):
            print(flota2[i], flota[i].get_position())
            flota[i].move(random.randint(-50,50),random.randint(-50,50))
    z=z+1
