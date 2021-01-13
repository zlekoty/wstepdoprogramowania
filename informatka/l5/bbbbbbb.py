x=[1,3,2]
n=len(x)
y=x.copy()
def b(x):
    for i in range(n-1):
        for j in range(i,n):
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
                print(x)
            else:
                x[i],x[j]=x[i],x[j]
