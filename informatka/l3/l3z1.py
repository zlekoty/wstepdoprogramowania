x=input('podaj tekst: ')
x=x.upper()
x1=list(x)
x1.sort()
#def u0(x1):
 #   spacja=x1[0]
  # while sss>0:
   #     x1.remove(spacja)
    #    if sss==0:
     #       break


#usuwanie powielonych elementów z x
def u(x1):
    z=0
    while z<=len(x1): 
        y=x1[z]
        a=x1.count(y)
        if a>1:
            x1.remove(y)
        if a==1:
            z=z+1
        if z==len(x1):
            break
u(x1)
x2=list(x)
x2.sort()
v=[]
#utworzenie listy indeksów x1
for w in x1:
    c=x2.count(w)
    v.append(c)
    
x3=dict()
b=0
#połączenie indeksów z x1
for o in x1:
    x3[o]=v[b]
    b=b+1

v.sort(reverse=True)
hb=0
i=0
#przypisanie wartości indeksu do wartości x3
for ha in v:
    if ha==hb:
        pass
    else:
        hb=ha
        for s in x3:
            if x3[s]==ha:
                if i <=10:
                    print(s,ha,'*'*ha)
                    i=i+1
#import matplotlib.pyplot as plt
#plt.plot(s,ha)
#plt.show
