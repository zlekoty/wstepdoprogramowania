x=input('łańcuch znaków: ')
y=input('szukana: ')
index=0
a=0
z=x.find(y,index)
while z<len(x):
    z=x.find(y,index)
    a=a+1
    index=z+1
    if z==-1:
        break
print('ilość szukanego znaku:',a-1)

#druga opcja
x=input('łańcuch znaków: ')
y=input('szukana: ')
litera=y
count=0
for y in x:
    if litera==y:
        count=count+1
print(count)
