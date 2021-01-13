def posortowana(x):
    while 1==1:
        y=x.copy()
        n=len(x)
        try:
            for i in range(n-1):
                for j in range(i,n):
                    if x[i]>x[j]:
                        x[i],x[j]=x[j],x[i]                   
            if x==y:
                print(x==y)
            else:
                for i in range(n-1):
                    for j in range(i,n):
                        if x[i]<x[j]:
                            x[i],x[j]=x[j],x[i]  
                print(x==y)
        except:
            print('błąd')
        break
posortowana([1,5,2,'a'])
posortowana([1,6,8])
posortowana([1,5,2])
posortowana([3,3,-1])
