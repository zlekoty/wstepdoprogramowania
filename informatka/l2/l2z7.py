def fibonacci(n):
    if n<3:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    
def wyrazy(n):
    while 1<=n:
        print(fibonacci(n))
        n=n-1
    return(' ')
x=eval(input("podaj liczbę naturalną: "))
print(wyrazy(x))

