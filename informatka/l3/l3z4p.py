x='N PBQR BS RGUVPNY ORUNIVBE SBE CNGVRAGF:1. QB ABG RKCRPG LBHE QBPGBE GB FUNER LBHE QVFPBZSBEG. Vaibyirzragjvgu gur cngvrag’f fhssrevat zvtug pnhfr uvz gb ybfr inyhnoyrfpvragvsvp bowrpgvivgl.2. OR PURRESHY NG NYY GVZRF. Lbhe qbpgbe yrnqf n ohfl naq gelvatyvsr naq erdhverf nyy gur tragyrarff naq ernffhenapr ur pna trg.3. GEL GB FHSSRE SEBZ GUR QVFRNFR SBE JUVPU LBH NER ORVAT GERNGRQ.Erzrzore gung lbhe qbpgbe unf n cebsrffvbany erchgngvba gbhcubyq.'
for a in x:
    b=ord(a)
    if b>=65 and b<=77:
        print(chr(b+13),end="")
    elif b>=78 and b<=90:
        print(chr(b-13),end="")
    elif b>=97 and b<=109:
        print(chr(b+13),end="")
    elif b>=110 and b<=122:
        print(chr(b-13),end="")
    else:
        print(a,end="")
print()
x="N zna, n cyna, n pnany: Cnanzn!"
for a in x:
    b=ord(a)
    if b>=65 and b<=77:
        print(chr(b+13),end="")
    elif b>=78 and b<=90:
        print(chr(b-13),end="")
    elif b>=97 and b<=109:
        print(chr(b+13),end="")
    elif b>=110 and b<=122:
        print(chr(b-13),end="")
    else:
        print(a,end="")
