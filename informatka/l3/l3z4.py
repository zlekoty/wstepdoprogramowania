x1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
x2=[]
a1=0
while a1<=25:
    x2.append(a1)
    a1=a1+1
a1=0
x3=dict()
for y in x1:
    x3[y]=x2[a1]
    a1=a1+1
a1=0
z=input('podaj tekst: ')
z=list(z.upper())
x4=dict()
x6=dict()
for y1 in z:
    if x1.count(y1)==0:
        pass
    else:
        if (x3[y1]+13)<=25:
            y2=x3[y1]+13
            x4[y2]=y1
            x6[y1]=y2
        else:
            y2=x3[y1]-13
            x4[y2]=y1
            x6[y1]=y2
a1=0
x5=dict()
for y3 in x2:
    x5[y3]=x1[a1]
    a1=a1+1
a1=0
for y4 in z:
    if x1.count(y4)==0:
        rot13=y4
    else:
        rot13=x5[x6[y4]]
    print(rot13,end="")








