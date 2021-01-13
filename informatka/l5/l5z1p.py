def rgbtohtml(tryplet):
    if 0<=tryplet[0]<=255 and 0<=tryplet[1]<=255 and 0<=tryplet[2]<=255 and len(tryplet)==3:
        if 0<=tryplet[0]<=15:
            tryplet[0]=hex(tryplet[0])
            tryplet[0]='0'+tryplet[0][2:]
        else:
            tryplet[0]=hex(tryplet[0])
            tryplet[0]=tryplet[0][2:]
        if 0<=tryplet[1]<=15:
            tryplet[1]=hex(tryplet[1])
            tryplet[1]='0'+tryplet[1][2:]
        else:
            tryplet[1]=hex(tryplet[1])
            tryplet[1]=tryplet[1][2:]
        if 0<=tryplet[2]<=15:
            tryplet[2]=hex(tryplet[2])
            tryplet[2]='0'+tryplet[2][2:]
        else:
            tryplet[2]=hex(tryplet[2])
            tryplet[2]=tryplet[2][2:]
        html='#'+tryplet[0]+tryplet[1]+tryplet[2]
        print(html.upper())
    else:
        print('błąd')
rgbtohtml([1,2,255])
rgbtohtml([0,444444444444,0])
rgbtohtml([1,2,255,3])
