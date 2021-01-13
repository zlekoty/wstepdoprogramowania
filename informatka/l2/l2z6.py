x=input('słowo1: ')
y=input('słowo2: ')
a=0
while a<min(len(x),len(y)):
  if x[a]==y[a]:
    print('takie same znaki na pozycji:',a)
    a=a+1
  elif x[a]!=y[a]:
        print('inne znak na pozycji:',a)
        a=a+1
