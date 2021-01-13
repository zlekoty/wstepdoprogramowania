def trojkat():
    a=eval(input('długość boku 1: '))
    b=eval(input('długość boku 2: '))
    c=eval(input('długość boku 3: '))
    from statistics import median
    if a<=0 or b<=0 or c<0:
        print('bok nie może być <= zero')
    elif min(a,b,c) + median([a,b,c]) <max(a,b,c):
        print('False')
    else:
        print('True')
