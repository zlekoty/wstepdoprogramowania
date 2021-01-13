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
        a=i/2
        b=int(a-int(a)+0.5)
        if b==1:
            f1=f
            print(f)
        else:
            f2=f
            print(f)
x=eval(input('podaj liczbę naturalną: '))
print('rekurencyjnie:')
fibrekur(x)
print('iteracyjnie: ')
fibiter(x)
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
