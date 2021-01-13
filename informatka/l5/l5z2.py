def htmltorgb(x):
    while x[0]=='#' and len(x)==7:
        try:
            r='0x'+x[1:3]
            g='0x'+x[3:5]
            b='0x'+x[5:7]
            r=int(r, base=16)
            g=int(g, base=16)
            b=int(b, base=16)
            rgb=tuple([r,g,b])
            print(rgb)
        except:
            print('błąd')
        break
    if x[0]!='#' or len(x)!=7:
        print('błąd')
htmltorgb('#123Ff9')
htmltorgb('#1234q6')
htmltorgb('#ddddddddd')
