x=eval(input('podaj liczbę: '))
y=eval(input('podaj liczbę: '))
def nwd(x,y):
    a=max(x,y)-min(x,y)
    if a==0:
        print(min(x,y))
    else:
        nwd(a,min(x,y))
print('największy wspólny dzielnik: ',nwd(x,y))
    
