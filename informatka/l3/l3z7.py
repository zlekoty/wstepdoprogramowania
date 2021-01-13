a=eval(input('a='))
b=eval(input('b='))
c=eval(input('c='))
print(a,'x^2 +',b,'x +',c,'= 0')
d=b*b-4*a*c
import math
import cmath
if a==0:
    if b!=0:
        print('x=',(-c)/b)
    if b==0:
        if c!=0:
            print('brak rozwiązań')
        if c==0:
            print('nieskończenie wiele rozwiązań')
    
while a!=0:
    if d>0:
        print('x1=',(-b-math.sqrt(d))/(2*a))
        print('x2=',(-b+math.sqrt(d))/(2*a))
    if d==0:
        print('x=',-b/2/a)
    if d<0:
        d= complex(0,math.sqrt(-d))
        print('x1=',(-b-d)/(2*a))
        print('x2=',(-b+d)/(2*a))
    break
