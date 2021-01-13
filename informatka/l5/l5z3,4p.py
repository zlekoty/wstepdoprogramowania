def fibrekur(n):
    def fibrekurA(n):
        if n<3:
            return 1
        else:
            return(fibrekurA(n-1)+fibrekurA(n-2))
    while 1<=n:
        print(fibrekurA(n))
        n=n-1
    return 

def fibiter(n):
    f1=1
    f2=1
    print(f1)
    print(f2)
    for i in range(0,n-2):
        f=f1+f2
        print(f)
        f2=f1
        f1=f
x=eval(input('podaj liczbę naturalną: '))

import time
def czas(n):
    start=time.time()
    fibrekur(n)
    koniec=time.time()
    t=start-koniec
    print('czas rekurencji: ',t)
    start=time.time()
    fibiter(n)
    koniec=time.time()
    t=start-koniec
    print('czas iteracji: ',t)
czas(x)
