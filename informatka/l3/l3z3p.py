x=input('podaj tekst: ')
for a in x:
    b=ord(a)
    if b>=65 and b<=77:
        print(chr(b+13),end="")
    elif b>=78 and b<=90:
        print(chr(b-13),end="")
    elif b>=97 and b<=109:
        print(chr(b+13),end="")
    elif b>=110 and b<=122:
        print(chr(b-13),end="")
    else:
        print(a,end="")
