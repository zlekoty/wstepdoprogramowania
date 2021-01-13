def nwd(x,y):
    a=max(x,y)-min(x,y)
    if a==0:
        return min(x,y)
    else:
        return nwd(a,min(x,y))
b=list(eval(input('podaj listę liczb: ')))
d=[]
for c in b:
    for c1 in b:
        if c1!=c:
           d.append(nwd(c1,c))
print(min(d))
        
