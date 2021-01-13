n=eval(input('liczba wierszy: '))
m=[]
r=[]
i=0
y=0
x=0
while i<n:
    m.append(0)
    r.append(0)
    i=i+1
while y<n:
    while x<y:
        if x==0:
            m[x]=1
            x=x+1
        elif x>0:
            m[x]=r[x]+r[x-1]
            x=x+1
    y=y+1
    print(m[0:x])
    x=0
    while x<y:
        r[x]=m[x]
        x=x+1
    x=0
