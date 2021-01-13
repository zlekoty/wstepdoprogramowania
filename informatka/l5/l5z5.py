def pal(x):
    n=x.upper()
    t=0
    for i in range(0,len(n)):
        if n[i]!=n[len(n)-(i+1)]:
            print('nie palindrom')
            break
        else:
            t=t+1
            if t==len(n):
                print('palindrom')
