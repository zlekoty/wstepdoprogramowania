x=input('podaj łańcuch znaków: ')
y=input('czego szukasz? ')
w=input('od którego miejsca zacząć poszukiwanie: ')
a=eval(w)
z=x.find(y)
while a<len(x):
    if x[a]==y:
      print('pozycja w łańcuchu znaków: ',a)
      a=a+1
    elif z==-1:
        print('brak znaku w łańcuchu')
        break
    else:
        a=a+1
