import math

"""def relaciofugg(szam1,szam2):
    eredmeny=""
    if szam1>szam2:
        eredmeny= ">"
    elif szam1<szam2:
        eredmeny="<"
    else:
        eredmeny="="
    return eredmeny"""

"""def relacioelj():"""


sugar=int(input("Add meg egy kör sugarát: "))

def kerulet():
    if sugar<0:
        print("hiba: A kör sugara nem pozitív!")
    else:
        return 2*sugar*math.pi

def terulet():
    return sugar**2*math.pi

print(f'{kerulet()}')
