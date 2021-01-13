x=eval(input('ilość gwiazdek w pierwszym rzędzie: '))
y=0
while x>0:
    print(y*' ',x*'*')
    print((y+1)*' ',(x-2)*'+')
    x=x-4
    y=y+2
