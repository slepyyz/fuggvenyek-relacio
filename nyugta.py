def fejlab(szoveg):
    diszsor()
    print(f'*{szoveg:^22}*')
    diszsor()

def tetel(aru,ar):
    print(f'{aru:<11}{ar:>11}Ft')

def misc(szoveg1,szoveg2):
    print(f'{szoveg1:<12}{szoveg2:>12}')

def diszsor(kar:str="*"):
    print(kar*24)

