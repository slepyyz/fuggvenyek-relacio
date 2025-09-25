hossz=50

def diszsor(kar:str="*"):
    print(kar*hossz)

def fejlab(szoveg):
    diszsor()
    print(f'*{szoveg:^{hossz-2}}*')
    diszsor()

def tetel(aru,ar):
    print(f'{aru:<{int(hossz/2-1)}}{ar:>{int(hossz/2-1)}}Ft')
    arak=[]
    arak.append(int(ar))
    return arak

def misc(szoveg1,szoveg2,disz):
    if szoveg1=="" and szoveg2=="":
        print(f'{int(hossz/2-3)*disz:<{int(hossz/2)}}{int(hossz/2-3)*disz:>{int(hossz/2)}}')
    else:
        print(f'{szoveg1:<{int(hossz/2)}}{szoveg2:>{int(hossz/2)}}')







fejlab("Nyugta")
tetel("tetel1","1234.20")
tetel("tetel2","45.12")
tetel("tetel3","232.35")
diszsor("=")
tetel("Összesen:","1511.67")
tetel("Szervízdíj","151.17")
diszsor("=")
tetel("Fizetendő:","1662.84")
misc("","","-")
misc("Dátum","Név","")
fejlab("Ceg")